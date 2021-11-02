import os

folder_root = 'some_data'
dictionary={ 100:(), 1000:(), 10000:(),100000:()}
way= os.walk(folder_root)
files= []
files_name=[]
for i in os.walk(folder_root):
    files.append(i[2])
    for m in files:
        for o in m:
            files_name.append(o)
# print(files_name)


'''Чуть позже изменю пул'''






# print(way_2)
# for i in way_2:
#     i.(list_files)
#     print(list_files)
# for i in way:
#
#     print(i)
#     b=os.stat(os.path.join(way, i))





# '''................................................................................'''
# amount=sum(1 for i in way)
# print('Файлов в папке: ', amount) # сколько файлов в папке (Файлов в папке:  1000)
# '''................................................................................'''
# storage= (os.stat('some_data').st_size)
# print('Папка весит :', storage,'байт') # размер папки (Папка весит : 327680 байт)

