#1072 это номер русской буквы а
#1040 это номер русской буквы А
#97 номер англ буквы а z- 122
#65 - A


(4)
import random

num_a = int(input('Диапозон случайного числа: '))
num_b=int(input('Диапозон случайного числа: '))

num_c= random.randint(num_a,num_b)

num_u=random.uniform(num_a,num_b)

sym_ot=input('Диапозон случайной буквы: ')
sym_do=input('Диапозон случайной буквы: ')

symbol=random.randint(ord(sym_ot),ord(sym_do))

print(f'\nСлучайное целое число:{num_c}\n'
      f'Случайное вещественное число:{num_u}\n'
      f'Случайный символ от {sym_ot} до {sym_do}: {chr(symbol)}')



