list_a= ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_b=[]

for n in list_a:

    if n.isdigit():
        list_b.extend(['"', f'{int(n):02}', '"'])

    elif (n.startswith('+') or n.startswith('-')) and n[1:].isdigit():
        list_b.extend(['"', f'{n[0]}{int(n[1:]):02}', '"'])

    else:
        list_b.append(n)

list_b=" ".join(list_b)
print(list_b)



#9.10.21 Зырянов Александр
# Основу понял сам, надо почитать за фишки format
