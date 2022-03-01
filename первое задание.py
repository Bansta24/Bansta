"1- логический математический алгоритм"# 2 минуса первого кода - нет гибкости под длинные числа. Только 3х значные
                                #числа и занимает больше места - создает 3 лишние переменные и ссылки на них
"2- цикл по числу" # когда цикл решает обе задачи, он в ону переменную сразу делает сумму, а в другую произмедение
            # не занимая лишнюю память. А так же позволяет писать более длинные числа


#1
user_numb=int(input("Ваше число: "))

first_num=user_numb // 100
second_num=user_numb//10%10
third_num=user_numb % 10

summ=first_num+second_num+third_num
print(f'Сумма: {summ}')

multi=first_num*second_num*third_num
print(f'Произведение: {multi}')

#2
n = int(input())

suma = 0
mult = 1

while n > 0:
    num = n % 10
    suma = suma + num
    mult = mult * num
    n = n // 10

print(f'Сумма: {suma}')
print(f'Произведение: {mult}')
