# limit - формальный параметр функции print_numbers
def print_numbers(limit):
    for i in range(limit):
        print(i)

# Здесь вызывается функция print_numbers, а её формальный
# параметр limit замещается фактическим параметром 10
print_numbers(10)