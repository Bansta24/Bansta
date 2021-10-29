from requests import *
import sys
import collections
import decimal
decimal.getcontext().prec=3

url= get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text
with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
   f.write(url)
   f.close()
data=[]
with open('nginx_logs.txt') as f:
   for line in f:
      splited=line.split()
      data.append((splited[0],splited[5].replace('"',''), splited[6]))
   #print(data)

print('\n',decimal.Decimal(sys.getsizeof(data)) /2048, 'мегабайт занимает данный список')

###########################################################################
spamer = collections.Counter(data).most_common()[0]
print(spamer)
print(f'Спапер : {spamer[0][0]}  \n  Скачал: {spamer[-1]} раз' ) # Спамер
########################################################################

i=sum(1 for element in url)
print('Зафискированно всего скачиваний: ',i)

# понимаю что надо через генератор, чтобы выводил,
# но не сохранял, посижу над этим после дедлайна, ибо срок поджимает



