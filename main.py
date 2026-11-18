from loan_manager import (
    add_loan,
    view_loans,
    view_loan_summary,
    delete_loan
)

from payment_manager import (
    record_payment,
    view_payment_history
)


def main():
    while True:
        print("\n====================================")
        print("       PERSONAL LOAN EMI TRACKER")
        print("====================================")

        print("1. Add New Loan")
        print("2. View All Loans")
        print("3. View Loan Summary")
        print("4. Record EMI Payment")
        print("5. View Payment History")
        print("6. Delete Loan")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_loan()

        elif choice == "2":
            view_loans()

        elif choice == "3":
            view_loan_summary()

        elif choice == "4":
            record_payment()

        elif choice == "5":
            view_payment_history()

        elif choice == "6":
            delete_loan()

        elif choice == "7":
            print("Thank you for using Loan EMI Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
