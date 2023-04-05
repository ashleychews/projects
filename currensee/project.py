import csv
from currency_symbols import CurrencySymbols
from datetime import datetime

def main():
    try:
        amount, initial_currency, target_currency, date = getinput()
        converted_amount = convert(amount, initial_currency, target_currency, date)
        isymbol = symbols(initial_currency)
        tsymbol = symbols(target_currency)
        print(f"{isymbol}{amount} {initial_currency} equals {tsymbol}{converted_amount} {target_currency} on {date}")
    except ValueError as e:
        print(str(e))  # print the error message from convert()
    except Exception as e:
        print(f"Error: {e}")

def getinput():
    amount = float(input("Input Amount: ").strip()) #amount user wants to convert
    initial_currency = input("Input Currency code to be converted: ").upper().strip()
    target_currency = input("Input Currency code to be converted to: ").upper().strip()
    date_input = input("Enter date (DD/MM/YYYY): ")
    date = datetime.strptime(date_input, "%d/%m/%Y").strftime("%d/%m/%Y")

    return amount, initial_currency, target_currency, date

def convert(amount, initial_currency, target_currency, date):
    with open('exchange_rates.csv') as f:
        reader = csv.DictReader(f)
        initial_exchange_rate = None
        target_exchange_rate = None
        for row in reader:
            if row['currency'] == initial_currency and row['date'] == date:
                initial_exchange_rate = float(row['value'])
            elif row['currency'] == target_currency and row['date'] == date:
                target_exchange_rate = float(row['value'])
            if initial_exchange_rate is not None and target_exchange_rate is not None:
                initial_amount = amount / initial_exchange_rate
                converted_amount = initial_amount * target_exchange_rate
                return converted_amount
        raise ValueError("Invalid currency or date")

def symbols(currency):
    return CurrencySymbols.get_symbol(currency)

if __name__ == '__main__':
    main()
