import pandas as pd
import csv
import os

def adding():
    date = input("enter date (YYYY-MM-DD): ")
    category = input("enter the category of spending: ")
    money = float(input("enter the amount: "))

    file_exists = os.path.isfile("expense_data.csv")
    file_empty = (not file_exists) or os.path.getsize("expense_data.csv") == 0

    with open("expense_data.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if file_empty:
            writer.writerow(["date", "category", "money"])

        writer.writerow([date, category, money])

    df = pd.read_csv("expense_data.csv")

    df.columns = df.columns.str.lower().str.strip()

    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d",errors="coerce").dt.date
    df["category"] = df["category"].str.lower().str.strip()
    df["money"] = pd.to_numeric(df["money"], errors="coerce").fillna(0)
    df["date"] = df["date"].fillna("invalid date")

    df.to_csv("expense_data.csv",index=False)


    print("Data added successfully")

if __name__ == "__main__":
    pass 
