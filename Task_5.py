# Реализовать структуру « Рейтинг » , представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если
# в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
# значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
user_number = int(input('Введите натуральное число - новый элемент рейтинга: '))

if user_number in my_list:
    my_list.insert(my_list.index(user_number) + my_list.count(user_number), user_number)
elif user_number > my_list[0]:
    my_list.insert(0, user_number)
else:
    my_list.append(user_number)

print(my_list)