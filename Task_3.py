# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

user_month = int(input('Введите месяц цифрой: '))

# dict

dict_seasons = {
    '1': 'зима',
    '2': 'весна',
    '3': 'лето',
    '4': 'осень'
}

if 0 < user_month < 3 or user_month == 12:
    print(dict_seasons['1'])
elif 2 < user_month < 6:
    print(dict_seasons['2'])
elif 5 < user_month < 9:
    print(dict_seasons['3'])
elif 8 < user_month < 12:
    print(dict_seasons['4'])

# list

list_seasons = ['зима', 'весна', 'лето', 'осень']

if 0 < user_month < 3 or user_month == 12:
    print(list_seasons[0])
elif 2 < user_month < 6:
    print(list_seasons[1])
elif 5 < user_month < 9:
    print(list_seasons[2])
elif 8 < user_month < 12:
    print(list_seasons[3])