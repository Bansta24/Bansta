# Задание 2
numbs = list (range(1,1000,2))
degree=[i**3 for i in numbs]

first_list= []
second_list=[]


for i in degree:
    if sum(map(int, str(i)))  % 7 ==0:
        first_list.append(i)
print(sum(first_list))

degree=[i+17 for i in degree]
for i in degree:
    if sum(map(int, str(i)))  % 7 ==0:
        second_list.append(i)
print(sum(second_list))





