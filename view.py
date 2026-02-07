#code for view spendings
import pandas as pd

def view():
    df = pd.read_csv("expense_data.csv")

    df["category"] = df["category"].str.lower().str.strip()

    print("------ your expenses ------")
    print(df)

if __name__ == "__main__":
    pass