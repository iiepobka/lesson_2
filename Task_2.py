# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать
# функцию input().

user_list = []
item = None

while item != 'stop_enter':
    item = input('Введите элемент списка (для остановки ввода введите stop_enter): ')
    user_list.append(item)
else:
    user_list.remove('stop_enter')

if len(user_list) % 2 == 0:
    for item in range(0, len(user_list), 2):
        user_list[item], user_list[item + 1] = user_list[item + 1], user_list[item]

    # Или так, но кода больше
    '''for item in range(1, len(user_list), 2):
        user_list.append(user_list[1])
        user_list.append(user_list[0])
        user_list.remove(user_list[1])
        user_list.remove(user_list[0])'''
else:
    for item in range(0, len(user_list) - 1, 2):
        user_list[item], user_list[item + 1] = user_list[item + 1], user_list[item]

    # Или так, но кода больше
    '''for item in range(1, len(user_list) - 1, 2):
        user_list.append(user_list[1])
        user_list.append(user_list[0])
        user_list.remove(user_list[1])
        user_list.remove(user_list[0])
    user_list.append(user_list[0])
    del user_list[0]'''

print(user_list)