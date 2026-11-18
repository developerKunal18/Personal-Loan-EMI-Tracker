from config import LOANS_FILE
from storage import load_data, save_data
from emi_calculator import (
    calculate_emi,
    calculate_total_payment,
    calculate_total_interest,
    calculate_outstanding_balance
)
from utils import (
    get_next_id,
    get_positive_number,
    get_positive_integer,
    get_date,
    print_line
)


def add_loan():
    loans = load_data(LOANS_FILE)

    name = input("Enter loan name: ").strip()

    if not name:
        print("Loan name is required.")
        return

    principal = get_positive_number("Enter loan amount: ₹")
    annual_rate = get_positive_number(
        "Enter annual interest rate (%): "
    )
    months = get_positive_integer(
        "Enter loan duration in months: "
    )
    start_date = get_date(
        "Enter loan start date (YYYY-MM-DD): "
    )

    emi = calculate_emi(principal, annual_rate, months)

    loan = {
        "id": get_next_id(loans),
        "name": name,
        "principal": round(principal, 2),
        "annual_rate": annual_rate,
        "months": months,
        "start_date": start_date,
        "emi": emi
    }

    loans.append(loan)
    save_data(LOANS_FILE, loans)

    total_payment = calculate_total_payment(emi, months)
    interest = calculate_total_interest(
        principal, emi, months
    )

    print("\nLoan added successfully!")
    print(f"Monthly EMI: ₹{emi:.2f}")
    print(f"Total payment: ₹{total_payment:.2f}")
    print(f"Total interest: ₹{interest:.2f}")


def view_loans():
    loans = load_data(LOANS_FILE)

    print_line()
    print("REGISTERED LOANS")
    print_line()

    if not loans:
        print("No loans found.")
        return

    for loan in loans:
        print(f"ID: {loan['id']}")
        print(f"Name: {loan['name']}")
        print(f"Principal: ₹{loan['principal']:.2f}")
        print(f"Interest Rate: {loan['annual_rate']}%")
        print(f"Duration: {loan['months']} months")
        print(f"Monthly EMI: ₹{loan['emi']:.2f}")
        print(f"Start Date: {loan['start_date']}")
        print_line()


def get_loan_by_id(loan_id):
    loans = load_data(LOANS_FILE)

    for loan in loans:
        if loan["id"] == loan_id:
            return loan

    return None


def view_loan_summary():
    loans = load_data(LOANS_FILE)

    if not loans:
        print("No loans available.")
        return

    try:
        loan_id = int(input("Enter loan ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    loan = get_loan_by_id(loan_id)

    if not loan:
        print("Loan not found.")
        return

    from config import PAYMENTS_FILE

    payments = load_data(PAYMENTS_FILE)

    loan_payments = [
        payment for payment in payments
        if payment["loan_id"] == loan_id
    ]

    paid_count = len(loan_payments)
    pending_count = max(loan["months"] - paid_count, 0)

    paid_amount = sum(
        payment["amount"] for payment in loan_payments
    )

    outstanding = calculate_outstanding_balance(
        loan, payments
    )

    print_line()
    print("LOAN SUMMARY")
    print_line()

    print(f"Loan: {loan['name']}")
    print(f"Principal: ₹{loan['principal']:.2f}")
    print(f"Monthly EMI: ₹{loan['emi']:.2f}")
    print(f"Total installments: {loan['months']}")
    print(f"Paid installments: {paid_count}")
    print(f"Pending installments: {pending_count}")
    print(f"Total amount paid: ₹{paid_amount:.2f}")
    print(f"Outstanding balance: ₹{outstanding:.2f}")


def delete_loan():
    loans = load_data(LOANS_FILE)

    try:
        loan_id = int(input("Enter loan ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    loan = next(
        (item for item in loans if item["id"] == loan_id),
        None
    )

    if not loan:
        print("Loan not found.")
        return

    confirm = input(
        f"Delete loan '{loan['name']}' and its payment history? (y/n): "
    ).strip().lower()

    if confirm != "y":
        print("Deletion cancelled.")
        return

    updated_loans = [
        item for item in loans
        if item["id"] != loan_id
    ]

    from config import PAYMENTS_FILE

    payments = load_data(PAYMENTS_FILE)

    updated_payments = [
        payment for payment in payments
        if payment["loan_id"] != loan_id
    ]

    save_data(LOANS_FILE, updated_loans)
    save_data(PAYMENTS_FILE, updated_payments)

    print("Loan and its payment history deleted.")
