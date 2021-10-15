first_fraze = str(input('Введіть першу фразу: '))
second_fraze = str(input('Введіть другу фразу: '))

first_set = {i.lower() for i in first_fraze if i.isalpha()}
second_set = {i.lower() for i in second_fraze if i.isalpha()}

print(f'Множина літер першої фрази: {first_set}, другої: {second_set}.')

if second_set == first_set:
    print('З літер першої фрази можна скласти другу.')
else:
    print('З літер першої фрази неможливо скласти другу.')