def calculate_emi(principal, annual_rate, months):
    monthly_rate = annual_rate / (12 * 100)

    if monthly_rate == 0:
        return round(principal / months, 2)

    factor = (1 + monthly_rate) ** months

    emi = (
        principal
        * monthly_rate
        * factor
        / (factor - 1)
    )

    return round(emi, 2)


def calculate_total_payment(emi, months):
    return round(emi * months, 2)


def calculate_total_interest(principal, emi, months):
    total_payment = calculate_total_payment(emi, months)

    return round(total_payment - principal, 2)


def calculate_outstanding_balance(loan, payments):
    paid_installments = len([
        payment for payment in payments
        if payment["loan_id"] == loan["id"]
    ])

    remaining_months = max(
        loan["months"] - paid_installments,
        0
    )

    if remaining_months == 0:
        return 0.0

    rate = loan["annual_rate"] / (12 * 100)

    if rate == 0:
        balance = loan["emi"] * remaining_months
    else:
        factor = (1 + rate) ** remaining_months

        balance = (
            loan["emi"]
            * (factor - 1)
            / (rate * factor)
        )

    return round(max(balance, 0), 2)
