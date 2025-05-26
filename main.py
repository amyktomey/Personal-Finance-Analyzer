import csv
from datetime import datetime

#column headers  ['transaction_id','date','customer_id','amount','type','description']
#def load_transactions(filename='financial_transactions.csv'):
def load_transactions(filename='transactions_test_file.csv'):
    """Load transactions from a CSV file into a list of dictionaries."""
    transactions = []
# Open file with 'with' statement
    with open(filename) as csvdatafile:    
#  Use csv.DictReader and create dictionary with all fields
        for line in csv.DictReader(csvdatafile):
            print(line)
            print("fine")
        for line in csvdatafile:
            print("huh?")
            line = line.replace("\n","") 
            print("hey")
            parts = line.split(",")
            print("cool")
            print(line)
            print("let's go")
            print(parts)
#   Parse date with datetime.strptime
            print("yikes")
            date = datetime.strptime([date], '%Y-%m-%d')
            print("We got this!") #another check here
    #   Make amount negative for 'debit'
            for type in csvdatafile:
                while type == "debit":
                    amount = amount * -1
                    print(amount) #test for change
                else:
                    continue
                print("So far, so good!")
    #   Add to transactions
            trans_count = 0
            description = csvdatafile(description)
            transaction = {
                'date': date,
                'amount': amount,
                'description': description
            }
            transactions.extend(transaction)
# Print the number of loaded transactions.
            trans_count += 1
        return transactions 
"""     try:
# Catch FileNotFoundError, ValueError
    except FileNotFoundError:
        print("File not found")
    except csv.Error as ooops:
        print(f"CSV error: {ooops}")  

 """
load_transactions()
