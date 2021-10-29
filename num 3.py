import itertools
import json
from string import *
out_dict={}
with open('users.csv', encoding='utf-8') as user:
    with open('hobby.csv',  encoding='utf-8') as hobby:
        len_user= sum(1 for line in user)
        len_hobby = sum(1 for line in hobby)

        if len_user<len_hobby:
            exit(1)

        user.seek(0)
        hobby.seek(0)

        for line_user, line_hobby in itertools.zip_longest(user,hobby):
            out_dict[line_user.strip()] = line_hobby.strip() if \
                line_hobby is not None else len_hobby

with open ('task3.json', 'w', encoding= 'utf-8') as f:
    json.dump(out_dict, f, ensure_ascii=False)
print(out_dict)


