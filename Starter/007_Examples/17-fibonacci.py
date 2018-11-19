# Числа Фибоначчи

# Количество чисел в последовательности
n = 10
# Список чисел Фибоначчи (изначально - две единицы)
fibs = [1, 1]

# Повторяем n - 2 раз, так как два числа уже в списке
for i in range(n - 2):
    # Добавляем сумму двух последних чисел
    fibs.append(fibs[i] + fibs[i + 1])

# Вывод списка на экран
print(fibs)