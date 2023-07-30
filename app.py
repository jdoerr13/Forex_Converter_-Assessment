from flask import Flask, render_template, request, session, redirect
import requests
from forex_python.converter import CurrencyRates, CurrencyCodes
# from flask_debugtoolbar import DebugToolbarExtension

# app.config["SECRET_KEY"] = "123456789"

app = Flask(__name__)
# app.config['SECRET_KEY'] = "never-tell!"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# debug = DebugToolbarExtension(app)

# Create an instance of CurrencyCodes to get currency options
c = CurrencyCodes()
currency_options = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD', 'KRW', 'SGD', 'NOK', 'MXN', 'INR', 'RUB', 'ZAR', 'TRY', 'BRL', 'TWD', 'DKK', 'PLN', 'THB', 'IDR', 'HUF', 'CZK', 'ILS', 'CLP', 'PHP', 'AED', 'COP', 'SAR', 'MYR', 'RON', 'KES', 'NGN', 'PKR', 'IQD', 'QAR', 'EGP', 'VND', 'BDT', 'OMR', 'LKR', 'UAH', 'UGX', 'KZT', 'GHS', 'BYN', 'JOD', 'AZN', 'DZD', 'MAD', 'XOF', 'TZS', 'XAF', 'SGD']

# currency_symbols = [c.get_symbol(code) for code in currency_options]

# # Print the list of currency symbols
# print(currency_symbols)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert_currency():
    base_currency = request.form['base_currency']
    target_currency = request.form['target_currency']
    amount = float(request.form['amount']) #float is not necessary be I am using input type="number" in HTML, but good practice, esp for testing


    try:
# Validate currency codes
        c = CurrencyCodes() #make sure we are using the methods from the forex_python library- must create an instance first to access!
        if not (c.get_currency_name(base_currency) and c.get_currency_name(target_currency)):
            raise ValueError('Invalid currency code.')

# Validate amount as a valid float
        amount = float(amount)

# Make API call to the ExchangeRate API
        api_url = f'https://api.exchangerate.host/convert?from={base_currency}&to={target_currency}&amount={amount}' #required parameters
        response = requests.get(api_url) #pull JSON format response
        print(response.json()) #make sure this is working!!
        data = response.json() #convert it into python
        exchange_rate = data['info']['rate']
        print(f'Exchange Rate: {exchange_rate}')

        result = data['result']
        error_msg = None #Placeholder var before error handeling indicating no error message present at the beginning. So if no error the except block is skipped

 
# Get the currency symbol for the target currency
        base_currency_symbol = c.get_symbol(base_currency)
        target_currency_symbol = c.get_symbol(target_currency)
        base_currency_name = c.get_currency_name(base_currency)
        target_currency_name = c.get_currency_name(target_currency)

# Format the result with the appropriate currency symbol and rounded to two decimal places
        converted_result = f'{base_currency_symbol}{amount:.2f} {base_currency_name} equals {target_currency_symbol} {result:.2f} {target_currency_name}'#.2f - takes the value of result, format it as a floating-point number with two decimal places, and insert it into the string.

    except ValueError as e:
        result = None #set to none to indicate that the conversion process failed.
        converted_result = None
        error_msg = str(e) #capture the error messages converted to a string and store in variable
        print("Error Message:", error_msg)

    return render_template('index.html', currency_options=currency_options, result=result, converted_result=converted_result, error_msg=error_msg)


 