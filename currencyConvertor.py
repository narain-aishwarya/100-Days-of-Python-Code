#forex_python.converter is a free foreign exchange rates and currency convertor.
#from forex_python.converter import CurrencyRates
c = CurrencyRates()
amount = int(input("Enter Amount: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
print(from_currency, "To ", to_currency, amount)
result =c.convert(from_currency, to_currency, amount)
print(result)
