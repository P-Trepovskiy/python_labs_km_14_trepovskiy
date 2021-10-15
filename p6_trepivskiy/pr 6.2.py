main_dict = {'Newfoundland': 'A', 'Nova Scotia': 'B', 'Prince Edward Island': 'C', 'New Brunswick': 'E',
             'Quebec': ['G', 'H', 'J'], 'Ontario': ['K', 'L', 'M', 'N', 'P'], 'Manitoba': 'R', 'Saskatchewan': 'S',
             'Alberta': 'T', 'British Columbia': 'V', 'Nunavut': 'X', 'Northwest Territories': 'X', 'Yukon': 'Y'}

users_index = str(input('Введіть поштовий індекс: '))
if not users_index[0].isalpha() or not users_index[1].isdigit() or type(users_index[2]) == str:
    print('Помилка при введенні.')
    exit()

users_province = ''
for i in main_dict.values():
    if i == users_index[0].upper():
        users_province = list(main_dict.keys())[list(main_dict.values()).index(i)]
    if type(i) == list:
            if users_index[0].upper() in i:
                users_province = list(main_dict.keys())[list(main_dict.values()).index(i)]

if users_province == '':
    print('Такої провінції немає.')
    exit()

if int(users_index[1]) == 0:
    print(f'Адресат знаходиться у сільскій місцевості провінції {users_province}')
else:
    print(f'Адресат знаходиться у міській місцевості провінції {users_province}')
