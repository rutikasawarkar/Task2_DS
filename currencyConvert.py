

# if currency is not INR then convert it to INR.oct
# if currency is INR then convert it to USD
#print(jResp['data']['rates']['INR'])

# op = 
#  {
#         'name':'TCS',
#         'curren_price': 3000,
#         'USD_price': 34
#     }




import requests as rq

cUrl = "https://api.coinbase.com/v2/exchange-rates"

cHeaders = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

stockData = [
    {
        'name':'TCS',
        'current_price': 3000,
        'currency': 'INR',
        'USD_price': '?'
    },
    {
        'name':'GOOG',
        'current_price': 166.82,
        'currency': 'USD',
        'USD_price': '?'
    },
    {
        'name':'DBS_GROUP',
        'current_price': 39.18,
        'currency': 'SGD',
        'USD_price': '?'
    },
    { 
        'name':'Trident',
        'current_price': 158.52,
        'currency': 'CNY',
        'USD_price': '?' 
    }
]

cResp = rq.get(url=cUrl, headers=cHeaders).json()

currencyData= cResp['data']['rates']
#print('currencyData:',currencyData)


def convert_currency(currencyData):
    for stocks in stockData:
        currency = stocks['currency']
        price = stocks['current_price']

        if currency == 'INR':
            Usd_rate = float(currencyData['INR'])
            stocks['USD_price']= round(price/ Usd_rate,2)
        elif currency =='USD':
            inr_rate = float(currencyData['INR'])
            stocks['USD_price']= round(price *inr_rate,2)
        else:
            stocks['USD_price']= 'Rates are not in the list'

convert_currency(currencyData)


for stocks in stockData:
    print(f'name ={stocks['name']}, current_price ={stocks['current_price']},currency = {stocks['currency']}, USD_price= {stocks['USD_price']}')