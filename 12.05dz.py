#3
def log_call(func):
    def wrapper(*args, **kwargs):
        returning = func(*args, **kwargs)
        print(f'Функція {func.__name__} приймає аргументи args {args}, '              
              f'та kwargs {kwargs}, та повертає {returning}')
        return returning
    return wrapper
@log_call
def temperature(C):
    return (C * 1.8) + 32
print(temperature(32))
print(temperature(40))
print(temperature(50))
