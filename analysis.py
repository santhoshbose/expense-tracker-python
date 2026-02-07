#code for analysis
import pandas as pd
def analysis():
    df = pd.read_csv("expense_data.csv")
    df["category"] = df["category"].str.lower().str.strip()
    grouped = df.groupby("category",as_index=False)["money"].sum()
    times = df.groupby("category").size()


    total = grouped["money"].sum()
    grouped["percentage"] = round((grouped["money"]/total)*100,2)
    grouped["no.of times"] = grouped["category"].map(times)

    maximum = grouped["money"].max()
    minimum = grouped["money"].min()
    average = grouped["money"].mean()
    max_category = grouped.loc[grouped["money"].idxmax(),"category"]
    min_category = grouped.loc[grouped["money"].idxmin(),"category"]
    max_times = grouped.loc[grouped["money"].idxmax(),"no.of times"]
    min_times = grouped.loc[grouped["money"].idxmin(),"no.of times"]
    max_perc = grouped.loc[grouped["money"].idxmax(),"percentage"]
    min_perc = grouped.loc[grouped["money"].idxmin(),"percentage"]
    avg_spent = (average/total)*100

    print(grouped)

    print("\nmaximum money spending on:")
    print("\tcategory :",max_category)
    print("\tamount :",maximum)
    print("\tno.of times :",max_times)
    print(f"\tpercentage : {max_perc:.2f}")

    print("\nminimum money spending on:")
    print("\tcategory :",min_category)
    print("\tamount :",minimum)
    print("\tno.of times :",min_times)
    print(f"\tpercentage : {min_perc:.2f}")

    print("\nyour average spendings :")
    print(f"\tamount : {average:.2f}")
    print(f"\tpercentage : {avg_spent:.2f}")

if __name__ == "__main__":
    pass