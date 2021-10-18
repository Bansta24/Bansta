nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

x=int(input('Сколько написать шуток'))

for i in range(x):
    import random

    first_word = random.choice(nouns)
    second_word = random.choice(adverbs)
    third_word =random.choice(adjectives)

    print(first_word.capitalize(), second_word, third_word)



