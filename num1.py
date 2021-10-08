# Задание 1
user_time=int(input(print('Введите время в секундах : ')))
day_constant =86400
hour_constant =3600
min_constant =60



title_list= ['день', 'дня', 'дней', 'час','часа', 'часов', 'минут', 'секунд']

day_title= None
hour_title = None

day_answer = user_time // day_constant

if day_answer == 1:
    day_title = title_list[0]
elif day_answer <5 and day_answer>1:
    day_title = title_list[1]
else:
    day_title= title_list[2]

hour_answer= (user_time - (day_constant * day_answer )) // hour_constant

if  hour_answer == 1 :
    hour_title = title_list [4]
elif hour_answer < 5 and hour_answer>1:
    hour_title = title_list[4]
else:
    hour_title= title_list[5]

min1=  ((user_time - (day_constant * day_answer)) - (hour_constant * hour_answer)) // min_constant

sec = (((user_time - (day_constant * day_answer)) - (hour_constant * hour_answer)))- (min_constant*min1)

print(day_answer, day_title, hour_answer, hour_title, min1,title_list[6] , sec, title_list[7])


#####################################################################################################################



