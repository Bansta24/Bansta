(6)
numb= int(input('Какую букву в русском алфавите вы хотите чтобы я вам показал? \n'))
if numb>32:
    print('В нашем алфавите 32 буквы')
else:
    numb_letter= 1071+numb
    print(chr(numb_letter).upper(),chr(numb_letter))

