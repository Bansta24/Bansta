names=['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА','токарь высшего разряда нИКОЛАй','директор аэлита']

lastNames = map(lambda name: name.split(' ')[-1], names)
for i in lastNames:
    print('Привет', i.capitalize())

#11.10.21 Зырянов Александр