import pandas as pd
import analysis
import view
import add_analysis
def reset_csv():
    headers = ["date","category","money"]
    df = pd.DataFrame(columns =headers)
    df.to_csv("expense_data.csv",index=False)
    print("old data cleared, starting new....")

def main():


    while True:
        
        print("\n\tADD       -----> 1")
        print("\tVIEW     -----> 2")
        print("\tANALYSIS -----> 3")
        print("\tEXIT     -----> 4")
        print("\tNEW       -----> 5")

        choice = int(input("\nenter your choice :"))
        if choice == 1:
            add_analysis.adding()
        elif choice == 2:
            view.view()
        elif choice == 3:
            analysis.analysis()
        elif choice == 4:
            print("Thank you for using the expense tracker. See you soon")
            break
        elif choice == 5:
            x = input("Are you sure? This will delete all the data(yes\no) :")
            if x.lower().strip() == "yes":
                reset_csv()
            continue
        else:
            print("unavailable option")

main()