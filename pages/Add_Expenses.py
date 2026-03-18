import streamlit as st
import pandas as pd
from datetime import date
import os

st.title("➕💸 Add Expenses")

file = "expenses.csv"

def load_expenses(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except (pd.errors.EmptyDataError, FileNotFoundError):
        df = pd.DataFrame(columns=["Date", "Category", "Amount", "Note"])
        df.to_csv(path, index=False)
        return df

# file load
load_expenses(file)

expense_date = st.date_input("Date", date.today())

category = st.selectbox(
    "Category", ["Food", "Travel", "Shopping", "Other"]
)

amount = st.number_input("Amount", min_value=0.0, step=1.0)

note = st.text_input("Note")

if st.button("Add Expense"):

    df = pd.read_csv(file)

    new_data = pd.DataFrame({
        "Date": [expense_date],
        "Category": [category],
        "Amount": [amount],
        "Note": [note]
    })

    df = pd.concat([df, new_data], ignore_index=True)

    df.to_csv(file, index=False)

    st.success("Expense added successfully")