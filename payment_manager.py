from config import LOANS_FILE, PAYMENTS_FILE
from storage import load_data, save_data
from utils import get_next_id, get_date, print_line


def record_payment():
    loans = load_data(LOANS_FILE)
    payments = load_data(PAYMENTS_FILE)

    if not loans:
        print("Add a loan first.")
        return

    print("\nAVAILABLE LOANS")

    for loan in loans:
        print(
            f"{loan['id']}. {loan['name']} "
            f"- EMI: ₹{loan['emi']:.2f}"
        )

    try:
        loan_id = int(input("\nEnter loan ID: "))
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

    existing = [
        payment for payment in payments
        if payment["loan_id"] == loan_id
    ]

    if len(existing) >= loan["months"]:
        print("All installments have already been recorded.")
        return

    payment_date = get_date(
        "Enter payment date (YYYY-MM-DD): "
    )

    if any(
        payment["payment_date"] == payment_date
        for payment in existing
    ):
        print("A payment is already recorded for this date.")
        return

    amount = loan["emi"]

    payment = {
        "id": get_next_id(payments),
        "loan_id": loan_id,
        "amount": amount,
        "payment_date": payment_date
    }

    payments.append(payment)
    save_data(PAYMENTS_FILE, payments)

    print("EMI payment recorded successfully!")
    print(f"Amount: ₹{amount:.2f}")


def view_payment_history():
    payments = load_data(PAYMENTS_FILE)
    loans = load_data(LOANS_FILE)

    print_line()
    print("PAYMENT HISTORY")
    print_line()

    if not payments:
        print("No payments recorded.")
        return

    loan_map = {
        loan["id"]: loan["name"]
        for loan in loans
    }

    for payment in sorted(
        payments,
        key=lambda item: (item["payment_date"], item["id"])
    ):
        loan_name = loan_map.get(
            payment["loan_id"],
            "Deleted loan"
        )

        print(
            f"Payment ID: {payment['id']} | "
            f"Loan: {loan_name} | "
            f"Amount: ₹{payment['amount']:.2f} | "
            f"Date: {payment['payment_date']}"
        )
