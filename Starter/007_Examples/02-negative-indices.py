# Можно также использовать отрицательные индексы.
# В таком случае обход элементов начинается не с первого,
# а с последнего. Индекс последнего элемента списка – -1,
# предпоследнего – -2 и т.д.

# Создание списка чисел
my_list = [5, 7, 9, 1, 1, 2]

# Получение предпоследнего значения
pre_last = my_list[-2]  # pre_last == 1
print(pre_last)

# Вычисление суммы первого и последнего значений
result = my_list[0] + my_list[-1]
print(result)