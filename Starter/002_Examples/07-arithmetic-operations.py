import math  # импротируем модуль math

x = 3.265
# целое число, ближайшее целое снизу, ближайшее целое сверху
print(math.trunc(x), math.floor(x), math.ceil(x))

print(math.pi)  # константа пи
print(math.e)   # число Эйлера

y = math.sin(math.pi / 4)  # math.sin – синус
print(round(y, 2))

y = 1 / math.sqrt(2)  # math.sqrt – квадратный корень
print(round(y, 2))