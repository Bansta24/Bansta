tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
              'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

list_1= list(zip(tutors, klasses))
for i in list_1:
    print(i)

################################################################    Генератор
list_1=((tut,klass)for tut, klass in zip (tutors,klasses))
print(next(list_1))
print(next(list_1))
print(next(list_1))
print(next(list_1))
print(next(list_1))

############################################# Num 4
if len(tutors) > len(klasses):
    m=len(tutors) -( len(tutors) - len(klasses))
    while m < len(tutors):
       print(tutors[m],None)
       m+=1

############################################## Num 4 Генератор

import itertools as it
list_1=((tut,klass)for tut, klass in it.zip_longest(tutors,klasses))
print(next(list_1))
print(next(list_1))
print(next(list_1))
print(next(list_1))
print(next(list_1))
print(next(list_1))
print(next(list_1))



