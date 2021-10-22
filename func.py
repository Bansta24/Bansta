import requests
from decimal import *
from datetime import datetime

getcontext().prec = 5 #для decimal, сколько цифр после запятой в данном случае 5

def rate (valute):
    valute = valute.upper() #перевод ключ валюты в верхний регистр
    http = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text # текст сайта по которому в дальнейшем бдет искать ключи

    if valute not in http:
        return None

    rub = http[http.find('<Value>',http.find(valute)) +7: http.find('</Value>', http.find(valute))]
    # нахожднение подстроки в строке под название Value.
    #.find в скобках прописывается 

    date_time = http[http.find('Date="') + 6:http.find('"', http.find('Date="') + 6)].split('.')
    day, month, year = map(int, date_time)
    return f"{Decimal(rub.replace(',', '.'))}, {datetime (day=day, month=month, year=year)}"

print(rate(input('Введите название валюты: ')))

