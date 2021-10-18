num= {'one':'один','two':'два','three':'три','four':'четыре','five':'пять',
                'six':'шесть','seven':'семь','eight':'восемь','nine':'девять','ten':'десять'}
# word = input('Введите число на англиском:  ')

def num_translate_adv (word):
    if word[0].isupper():
        word=word.lower()
        return num[word].capitalize()
    else:
        return num[word]

print(num_translate_adv('One'))
print(num_translate_adv('one'))