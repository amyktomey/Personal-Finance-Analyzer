Capstone Project: Smart Personal Finance Analyzer
A Beginner-Friendly Python Project for Financial Management

Introduction
Welcome to the capstone project for Module 1 of the Code You Introduction to Python course! You’ve spent seven weeks learning Python, from printing messages to handling files and modules. Now, you’ll apply those skills in the Smart Personal Finance Analyzer, a command-line program that manages financial transactions. This project will help you build a portfolio-ready application to impress employers.

You’ll work with a CSV file called financial_transactions.csv, add and modify transactions, calculate financial summaries, and save your work. The instructions are clear, designed for beginners, with hints to guide you without giving full solutions. Even a 7th grader can follow along!

Project Plan
Complete this project with five Task s:

Explanatory Notes: Simple explanations of tasks and concepts.
Python Code Hints: Starter code to help you start.
Additional tasks to be completed: 2–4 tasks to reinforce learning. Review questions at the end solidify your understanding.
Assumed Knowledge
This project builds on:

Week 1: Printing, variables, input, arithmetic, formatting, conditionals, debugging.
Week 2: Loops, advanced conditionals, debugging control flow.
Week 3: Functions, string manipulation, formatting, debugging.
Week 4: Lists, iteration, function design, list operations, debugging.
Week 5: Dictionaries, tuples, algorithms, reference management, debugging.
Week 6: File reading/writing, error handling, validation.
Week 7: Modules, date/time handling, data processing, custom modules.
Refresh with the Course Contents and Github code if needed.

Getting Started
Ensure you have:

Python installed.
A text editor or IDE (e.g., VSCode, PyCharm).
The financial_transactions.csv file in the same folder as your Python script.
Input File: financial_transactions.csv
Input file is located here: https://github.com/RamaKattunga/Code-Notes/blob/main/financial_transactions.csv The financial_transactions.csv file contains financial transactions with these columns:

transaction_id: Unique ID (e.g., 1).
date: In YYYY-MM-DD format (e.g., 2020-10-26).
customer_id: Customer identifier (e.g., 926).
amount: Positive number (e.g., 6478.39).
type: “credit” (money received), “debit” (money spent), or “transfer” (money moved).
description: Transaction note (e.g., “Expect series shake art again our.”).
Example CSV Content:

transaction_id,date,customer_id,amount,type,description
1,2020-10-26,926,6478.39,credit,Expect series shake art again our.
2,2020-01-08,466,1255.95,credit,Each left similar likely coach take.
3,2019-09-02,110,7969.68,debit,Direction wife job pull determine leader move college.
New Terminology Explained
CRUD Operations: Four ways to manage data:
Create: Add a new transaction (e.g., a purchase).
Read: View transactions (e.g., list all credits).
Update: Change a transaction (e.g., fix a description).
Delete: Remove a transaction (e.g., delete a mistake).
Unit Testing: Checking if small code parts work correctly. For example, test if your program loads a transaction by using a sample CSV and verifying the output. You’ll do simple manual tests.
Task 1: Loading Transactions from a CSV File
Explanatory Notes
Week 6 taught you to read CSV files, which store data like spreadsheets. Your first task is to load financial_transactions.csv into a list of dictionaries. Validate data (e.g., correct date format) and handle errors (e.g., missing file) using Week 6’s error handling. Use Week 7’s date handling for dates and Week 4/5’s lists/dictionaries for storage.

Key Skills:

Reading CSV files (csv module, Week 6).
Handling errors (try-except, Week 6).
Storing data in lists/dictionaries (Weeks 4, 5).
Parsing dates (datetime, Week 7).
Debugging file operations (Weeks 1, 6).
Python Code Hint
import csv
from datetime import datetime

def load_transactions(filename='financial_transactions.csv'):
    """Load transactions from a CSV file into a list of dictionaries."""
    transactions = []
    # Open file with 'with' statement
    # Use csv.DictReader
    # For each row:
    #   Parse date with datetime.strptime
    #   Make amount negative for 'debit'
    #   Create dictionary with all fields
    #   Add to transactions
    # Catch FileNotFoundError, ValueError
    return transactions
Tips:

csv.DictReader reads rows as dictionaries.
Use datetime.strptime(date_str, '%Y-%m-%d') for dates.
Make amounts negative for ‘debit’ to reflect expenses.
Expected Output
A list of dictionaries, e.g.:

[
    {'transaction_id': 1, 'date': datetime(2020, 10, 26), 'customer_id': 926, 'amount': 6478.39, 'type': 'credit', 'description': 'Expect series shake art again our.'},
    {'transaction_id': 3, 'date': datetime(2019, 9, 2), 'customer_id': 110, 'amount': -7969.68, 'type': 'debit', 'description': 'Direction wife job pull determine leader move college.'}
]
Additional tasks to be completed
Print the number of loaded transactions.
Skip rows with invalid amounts and print a warning.
Test with a CSV containing one bad date and verify it’s skipped.
Log errors to errors.txt.
Task 2: Adding and Viewing Transactions
Explanatory Notes
Weeks 1–3 covered user input, conditionals, loops, and functions. This Task focuses on Create (adding transactions) and Read (viewing them) from CRUD. Adding uses Week 1’s input and Week 2’s validation, while viewing uses Week 2’s loops and Week 3’s formatting.

Key Skills:

User input (input(), Week 1).
Input validation (conditionals, Week 2).
Functions (Week 3).
Looping through lists (Week 2).
Formatting output (Weeks 1, 3).
Debugging interactions (Weeks 1, 2).
Python Code Hint
For adding:

def add_transaction(transactions):
    """Add a new transaction from user input."""
    # Prompt for date, customer_id, amount, type, description
    # Validate date, amount, type
    # Generate new transaction_id
    # Create dictionary and append
    pass
For viewing:

def view_transactions(transactions):
    """Display transactions in a table."""
    # Print header
    # Loop through transactions
    # Format each row
    pass
Tips:

Generate transaction_id by finding the max ID + 1.
Validate type as ‘credit’, ‘debit’, or ‘transfer’.
Use string formatting for table alignment.
Expected Output
Adding:

Enter date (YYYY-MM-DD): 2023-04-01
Enter customer ID: 500
Enter amount: 100.00
Enter type (credit/debit/transfer): debit
Enter description: Coffee shop purchase
Transaction added!
Viewing:

ID  | Date       | Customer | Amount   | Type   | Description
----|------------|----------|----------|--------|------------
1   | 2020-10-26 | 926      | 6478.39  | credit | Expect series...
3   | 2019-09-02 | 110      | -7969.68 | debit  | Direction wife...
Additional tasks to be completed
Reject invalid transaction types in add_transaction.
Add an option to view_transactions to filter by type.
Suggest customer IDs from existing transactions.
Format dates as “Oct 26, 2020” in view_transactions.
Task 3: Updating and Deleting Transactions
Explanatory Notes
This Task continues CRUD with Update and Delete. Modify or remove transactions using Week 2’s loops for options, Week 3’s functions for modularity, and Week 4’s list operations for changes. Week 1’s conditionals validate choices.

Key Skills:

Looping through lists (Week 2).
Functions (Week 3).
List operations (Week 4).
Conditionals (Week 1).
Debugging lists (Weeks 4, 5).
Python Code Hint
For updating:

def update_transaction(transactions):
    """Update a transaction’s details."""
    # Show transactions with numbers
    # Ask user to pick a number
    # Ask which field to change
    # Update field
    pass
For deleting:

def delete_transaction(transactions):
    """Delete a transaction."""
    # Show transactions with numbers
    # Ask user to pick a number
    # Confirm and remove
    pass
Tips:

Use enumerate for transaction numbers.
Validate transaction number input.
Confirm deletions with “Are you sure?”.
Expected Output
Updating:

1. 2020-10-26 | 926 | 6478.39 | credit | Expect series...
2. 2019-09-02 | 110 | -7969.68 | debit | Direction wife...
Select transaction (1-2): 1
Change which field? (description, type, amount): type
New type: transfer
Transaction updated!
Deleting:

1. 2020-10-26 | 926 | 6478.39 | transfer | Expect series...
2. 2019-09-02 | 110 | -7969.68 | debit | Direction wife...
Select transaction (1-2): 1
Are you sure? (yes/no): yes
Transaction deleted!
Additional tasks to be completed
Prevent invalid type updates in update_transaction.
Show transaction details before deletion.
Allow updating multiple fields at once.
Add a cancel option for updates/deletions.
Task 4: Analyzing Financial Data
Explanatory Notes
Weeks 5 and 7 introduced dictionaries and data processing. Calculate metrics like total credits, debits, and transfers, and group by type or customer ID. Use Week 2’s loops, Week 1’s arithmetic, and Week 5’s dictionaries.

Key Skills:

Looping (Week 2).
Dictionaries (Week 5).
Calculations (Week 1).
Formatting (Weeks 1, 3).
Algorithms (Week 5).
Python Code Hint
def analyze_finances(transactions):
    """Calculate and display financial summaries."""
    # Sum credits, debits, transfers
    # Group by type or customer_id
    # Print results
    pass
Tips:

Sum amounts by type using a dictionary.
Format numbers with f"${value:.2f}".
Handle transfers separately (neither income nor expense).
Expected Output
Financial Summary:
Total Credits: $6478.39
Total Debits: $7969.68
Total Transfers: $0.00
Net Balance: $-1491.29
By Type:
  Credit: $6478.39
  Debit: $7969.68
Additional tasks to be completed
Show the customer with the highest debit amount.
Calculate percentage of total amount by type.
Analyze transactions from 2022 only.
Save analysis to analysis.txt.
Task 5: Saving Transactions and Generating Reports
Explanatory Notes
Week 6 covered file writing. Save transactions to financial_transactions.csv and create a text report. Use Week 6’s file writing, Week 3’s formatting, and Week 1’s strings.

Key Skills:

Writing CSV files (Week 6).
File error handling (Week 6).
Formatting (Weeks 1, 3).
Debugging file output (Week 6).
Python Code Hint
For saving:

def save_transactions(transactions, filename='financial_transactions.csv'):
    """Save transactions to a CSV file."""
    # Open file for writing
    # Write header
    # Write each transaction
    pass
For reporting:

def generate_report(transactions, filename='report.txt'):
    """Generate a text report of financial summaries."""
    # Calculate metrics
    # Write to file
    pass
Tips:

Use csv.DictWriter for CSV output.
Convert dates to strftime('%Y-%m-%d').
Write report with file.write().
Expected Output
Saving:

Transactions saved to financial_transactions.csv
Report (report.txt):

Financial Summary
Total Credits: $6478.39
Total Debits: $7969.68
Total Transfers: $0.00
Net Balance: $-1491.29
By Type:
  Credit: $6478.39
  Debit: $7969.68
Additional tasks to be completed
Add a timestamp to the report filename (e.g., report_20250508.txt).
Back up the original CSV before saving.
Include transaction date range in the report.
Handle file-writing errors.
Main Program: Tying It All Together
Explanatory Notes
Create a menu using Week 2’s loops and Week 1’s conditionals. Organize code into a module (e.g., finance_utils.py) using Week 7’s module concepts for a professional touch.

Key Skills:

Menu loops (Week 2).
Conditionals (Week 1).
Functions (Week 3).
Modules (Week 7).
Python Code Hint
def main():
    transactions = []
    while True:
        print("\nSmart Personal Finance Analyzer")
        print("1. Load Transactions")
        print("2. Add Transaction")
        print("3. View Transactions")
        print("4. Update Transaction")
        print("5. Delete Transaction")
        print("6. Analyze Finances")
        print("7. Save Transactions")
        print("8. Generate Report")
        print("9. Exit")
        choice = input("Select an option: ")
        # Call functions based on choice
        if choice == '9':
            break
Tips:

Ensure transactions are loaded for tasks 2–8.
Move functions to a module and import them.
Expected Output
Smart Personal Finance Analyzer
1. Load Transactions
...
9. Exit
Select an option: 1
Transactions loaded!
Select an option: 9
Goodbye!
Testing Your Code
Test each function:

Load: Use a CSV with valid and invalid data.
Add: Add transactions and check the list.
Analyze: Verify calculations manually.
Save: Check CSV for correct data.
Ensure the following are completed
How does csv.DictReader help with CSV files?
Why use try-except for file operations?
How do functions improve code reuse?
Why use dictionaries for transactions?
How do loops aid in viewing transactions?
What’s the role of string formatting in reports?
How does datetime manage dates?
What errors might occur, and how to fix them?
How do modules organize code?
What features could enhance the analyzer?
Assessment Rubric
Criteria	Excellent (5)	Good (3)	Needs Work (1)
Functionality	All tasks work correctly	Most tasks work	Several tasks fail
Code Quality	Clear, commented, modular code	Readable, minor issues	Messy code
Error Handling	Handles all errors gracefully	Handles some errors	Crashes on errors
User Interaction	Intuitive menu and prompts	Functional but confusing	Hard to use
Concept Integration	Uses all week’s concepts	Uses most concepts	Misses key concepts
Bonus Challenges
Filter transactions by year (Week 7).
Use sets for unique customer IDs (Week 5).
Create a module for utilities (Week 7).
Generate random test transactions (Week 7).
Deliverables
Python script or Jupyter Notebook with code.
financial_transactions.csv with 20+ transactions.
Output files: report.txt, updated financial_transactions.csv.
README explaining how to run your program.
Show off your Python skills and build something amazing!