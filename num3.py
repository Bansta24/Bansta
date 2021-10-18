
name_in= ["Иван", "Мария", "Петр", "Илья"]

def thesaurus(names):
    notebook = {}
    for i in names:
        key = i[0]
        notebook.setdefault(key, [i])
        if i not in notebook[key]:
            notebook[key].append(i)
    print(notebook)

print(thesaurus(name_in))

####################################################
# notebook= {"И":{},"М":{},"П":{}}
# name_in= ["Иван", "Мария", "Петр", "Илья"]

# for i in name_in:
#     i.capitalize()  #для тех имен, что будут записаны с нижнего регистра
#     if i[0] =='И':
#         notebook['И']=i
#
#     elif i[0] =='М':
#         notebook['М']=i
#
#     else:
#         notebook['П']=i
#
# print(notebook)
#



















# def thesaurus ():
#     for i in name_in:
#         print(i[0])