# Если параметр name не задан, то name = 'Alex'
def hello(name='Alex'):
    print('Hello, ', name, '!', sep='')

hello('Python')
hello()