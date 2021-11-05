'''>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru'''

import re
EMAIL=re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')

def parsing_mail (email):
    info = EMAIL.findall(email)[0]
    if info:
        name, addres= info
    else:
        raise ValueError(f'wrong email: {email}')
    return name, addres

print(parsing_mail('bansta@bk.ru'))



# EMAIL=re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z])