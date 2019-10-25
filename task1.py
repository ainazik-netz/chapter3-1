text = input('Enter your text: ')
upper_letters = lower_letters = 0
text_length = len(text)
for i in text:
    if i.islower():
        lower_letters += 1
    elif i.isupper():
        upper_letters += 1
print('Процент всех прописных букв в тексте :' + str(round(lower_letters/text_length *100)) + '%')
print('Процент всех строчных букв в тексте:' + str(round(upper_letters/text_length*100))+ '%')   