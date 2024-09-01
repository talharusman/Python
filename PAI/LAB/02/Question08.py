import sys

# Define conversion rates relative to 1 USD
conversion_rates = {
    'USD': 1.0,     # US Dollar
    'EUR': 0.85,    # Euro
    'PKR': 287.95,  # Pakistani Rupee
    'INR': 82.45,   # Indian Rupee
    'JPY': 146.38   # Japanese Yen
}

def convert_currency(amount, from_currency, to_currency):
    amount_in_usd = amount / conversion_rates[from_currency]
    return amount_in_usd * conversion_rates[to_currency]

print("Welcome to the Currency Converter")
print("Available currencies: USD, EUR, PKR, INR, JPY")

from_currency = input("Enter the currency you want to convert from (USD, EUR, PKR, INR, JPY): ").upper()
if from_currency not in conversion_rates:
    print("Invalid currency! Please try again.")
    sys.exit()  # Exits the program if an invalid currency is entered

amount = float(input(f"Enter the amount in {from_currency}: "))

to_currency = input("Enter the currency you want to convert to (USD, EUR, PKR, INR, JPY): ").upper()
if to_currency not in conversion_rates:
    print("Invalid currency! Please try again.")
    sys.exit()  # Exits the program if an invalid currency is entered

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
