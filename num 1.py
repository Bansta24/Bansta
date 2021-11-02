import os
from os import *
#listdir() = ['Lib', 'num 1.py', 'pyvenv.cfg', 'Scripts', '__pycache__']
folder_get= (r'C:\Users\Bansta\PycharmProjects\Bansta_original\venv')
folder_main = ('my_project')
list_folder = {'settings' ,'mainapp','adminapp','authapp'}

if not os.path.exists(folder_main):
    os.mkdir(folder_main)  # ['Lib', 'my_project', 'num 1.py', 'pyvenv.cfg', 'Scripts', '__pycache__']

for i in list_folder: # саоздание папок в folder_main
    dir_path = os.path.join(folder_main,i )
    if not os.path.exists(dir_path): # если нет такой папки, то создает
       os.mkdir(dir_path)

print(os.getcwd())

#  Done

# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# 