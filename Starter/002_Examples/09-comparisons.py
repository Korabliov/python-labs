a = 2
b = 5

print(a < b)       # меньше
print(b > 3)       # больше
print(a <= 2)      # меньше или равно
print(b >= 7)      # больше или равно
print(a < 3 < b)   # двойное сравнение
print(a == b)      # равенство
print(a != b)      # неравенство
print(a is b)      # идентичность объектов в памяти
print(a is not b)  # a и b – разные объекты (хотя значения их могуть быть равны)

string = "some string"
second_string = string
third_string = input('Введите строку: ')
print(string is second_string)
print(string is third_string)