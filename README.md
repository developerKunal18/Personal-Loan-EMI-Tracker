# Personal Loan EMI Tracker

## About

A command-line Python application to manage personal loans,
calculate monthly EMIs, record payments, and track outstanding
loan balances.

## Features

- Add and manage multiple loans
- Calculate monthly EMI
- View loan details
- Record EMI payments
- Track paid and pending installments
- Calculate outstanding loan balance
- View payment history
- Delete loans

## Technologies Used

- Python
- JSON
- File Handling
- Functions
- Modules

## Project Structure

- main.py
- loan_manager.py
- emi_calculator.py
- payment_manager.py
- storage.py
- utils.py
- config.py
- requirements.txt
- .gitignore
- README.md
- data/
  - loans.json
  - payments.json

## How to Run

1. Clone the repository.
2. Open the project directory.
3. Run:

   python main.py

No external libraries are required.

## EMI Formula

EMI = P × R × (1 + R)^N / ((1 + R)^N - 1)

Where:

- P = Principal loan amount
- R = Monthly interest rate
- N = Loan duration in months

## Data Storage

Loan information and payment history are stored
locally using JSON files.

## Author

Python Projects Challenge
