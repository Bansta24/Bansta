first_numb=input('Первое число: ')
second_numb=input('Второе число: ')
third_numb=input('Третье число: ')

if second_numb<first_numb<third_numb or third_numb<first_numb<second_numb:
    print(first_numb)
elif first_numb<second_numb<third_numb or third_numb<second_numb<first_numb:
    print(second_numb)
else:
    print(third_numb)