word = str(input('Введіть перше слово: '))
words_list = []
while word != '':
    words_list.append(word)
    word = str(input('Введіть слово, або натисніть Enter для завершення вводу слів: '))
for i in words_list[0:len(words_list)-1]:
    print(f'{i}, ', end='')
print(f'and {words_list[len(words_list)-1]}')