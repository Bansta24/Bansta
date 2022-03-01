(5)
variant= int(input('Какой алфавит? 1.Русский 2.Английский:  '))

if variant==1:
    first_letter= int(ord(input('первая буква: ')))
    second_letter=int(ord(input('вторая буква: ')))

    print(f'Буква {chr(first_letter)} находится на {first_letter-1071}м месте в алфавите \n'
          f'Буква {chr(second_letter)} находится на {second_letter-1071}м месте в алфавите ')

    if (second_letter-first_letter)==1:
        print(f'Между ними нет букв')
    else:
        print(f'Между ними еще {abs(second_letter-first_letter)} букв')
elif variant==2:
    first_letter = int(ord(input('Первая буква: ')))
    second_letter = int(ord(input('Вторая буква: ')))

    print(f'Буква {chr(first_letter)} находится на {first_letter-96}м месте в алфавите \n'
          f'Буква {chr(second_letter)} находится на {second_letter-96}м месте в алфавите ')

    if (second_letter-first_letter)==1:
        print(f'Между ними нет букв')
    else:
        print(f'Между ними еще {abs(second_letter-first_letter)} букв')
else:
    print('Сказал же 1 или 2, заводи по новой')
