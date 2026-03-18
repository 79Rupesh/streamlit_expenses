import streamlit as st
import pandas as pd 

st.title("✅ Expense Dashboard")

file = "expenses.CSV"


def load_expenses(path:str)-> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except (pd.errors.EmptyDataError,FileNotFoundError):
        df = pd.DataFrame(columns=["Data","category","Amount","Note"])
        df.to_csv(path, index=False)
        return df
    
# load the data and handle the empty case gracefully 

df = load_expenses(file)

if df.empty:
    st.info("No expenses recorded yet. Add one from the sideebar .")
else:
    st.write("Category wise Expenses ")
    category_date=df.groupby("Category")["Amount"].sum()
    st.bar_chart(category_date)
    st.write("Expenses Distribution ")
    st.write(category_date)
    st.write("monthly Expenses")
    df["Date"]=pd.to_datetime(df["Date"])

    monthly = df.groupby(df["Date"].dt.month)["Amount"].sum()
    st.line_chart(monthly)



