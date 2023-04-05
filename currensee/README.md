# CurrenSee
## Video Demo:https://youtu.be/FTw-vtNHctI

## Description:
CurrenSee is a simple currency tracker programme designed to allow users to convert money for one currency to another based on the exchange rates at a given date. It makes use of the exchange rates provided in a CSV file. The programme prompts the user to enter several details before converting the amount and displaying the converted value with the currency symbols for the initial and target currencies.

Features
- Converts money from one currency to another
- Uses exchange rates from a CSV file that has been downloaded from https://www.kaggle.com/datasets/ruchi798/currency-exchange-rates. The dates ranges from 17/12/2021 to 3/4/2023
- Provides currency symbols for the input and output currencies
- If date is written in wrong format/country code is not available, an error will be shown

Usage
1. Enter the amount of money to be converted when prompted
2. Enter the currency code to be converted when prompted (e.g., USD, EUR, GBP)
3. Enter the currency code to convert to when prompted
4. Enter the date of the exchange rate to be used when prompted (DD/MM/YYYY format)
5. The converted amount and currency symbols will be displayed

An Example of how to use the CurrenSee:
Input Amount: 100
Input Currency code to be converted: USD
Input Currency code to be converted to: EUR
Enter date (DD/MM/YYYY): 17/12/2021
$100.0 USD equals €88.28067 EUR on 17/12/2021

Requirements
The Currency Converter requires Python 3.x to run. It also requires the following Python packages:

csv: to read exchange rate data from a CSV file
currency_symbols: to get the currency symbol for a given currency code
pytest: to run the test cases
To install the required packages, run the following command:
pip install -r requirements.txt
