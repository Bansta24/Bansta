src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
c=[]

for i in src:
    if src.count(i) == 1:
        c.append(i)
# print(result)
print(c)

#################################3
c=[i for i in src if src.count(i) == 1]
print(c)

######################################




