# Функция из прошлого примера
def print_numbers(limit):
    for i in range(limit):
        print(i)


# Любое логически завершённое действие следует помещать в функцию
def main():
    n = int(input('Введите n: '))
    print_numbers(n)


# Вызов главной функции
main()