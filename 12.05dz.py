#1
import time
def delay_decorator(func):
    def wrapper(*args , **kwargs):
        rezult = func(*args , **kwargs)
        for i in range(4):
         time.sleep(1.5)
         print(rezult)
        return rezult
    return wrapper
@delay_decorator
def sleepy(fuction):
    return fuction
sleepy('I love you')
