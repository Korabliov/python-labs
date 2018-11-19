# Эта функция возвращает аргумент, умноженный на два,
# если он отрицательный, или аргумент, умноженный на три,
# если он больше или равен нулю
def function(x):
    if x < 0:
        return x * 2
    else:
        return x * 3


def main():
    # Вывод значений функции в диапазоне [-3, 3]
    for i in range(-3, 4):
        y = function(i)
        print('function(', i, ') = ', y, sep='')


if __name__ == '__main__':
    main()