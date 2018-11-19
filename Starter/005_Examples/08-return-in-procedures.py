def hello(name):
    # Если имя пустое, выходим из функции
    if not name:
        return
    print('Hello, ', name, '!', sep='')


hello('Alex')
hello('')
hello('Python')