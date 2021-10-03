try:
    age = int(input('Введіть вік людини: '))
    if age > 2:
        dog_age = 21 + (age -2) * 4
    else:
        dog_age = 10.5 * age
    print(f'Пропорційний вік собаки дорівнює {dog_age}')
except ValueError:
    print('Неправильне введення.')