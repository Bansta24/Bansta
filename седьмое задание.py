(7)

first_side=int(input('Первая сторона: '))
second_side=int(input('Вторая сторона: '))
third_side=int(input('Третья сторона: '))

if (first_side+second_side)<=third_side or (second_side+third_side)<=first_side or (first_side+third_side)<=second_side :
    print('Треугольника не существует')
else:
    if first_side==second_side==third_side:
        print('Треугольник - равносторонний')
    elif first_side==second_side or second_side==third_side or first_side==third_side:
        print('Треугольник - равнобедренный')
    else:
        print('Треугольник разностороний')
