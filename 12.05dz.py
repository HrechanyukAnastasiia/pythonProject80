#4
import time

def timer(func):
    def wrapper(num):
        start_time = time.time()
        result = func(num)
        end_time = time.time()
        t = end_time - start_time
        print("Пройшло:", round(t, 2))
        return result
    return wrapper

@timer
def numbersss(num):
    time.sleep(2)
    x = 'Hе натуральне'
    y = 'Hатуральне'
    if num < 2:
        return x
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return x
    return y

number_1 = -6
number_2 = 2
number_3 = -7

print(f"Число {number_1}: {numbersss(number_1)}")
print(f"Число {number_2}: {numbersss(number_2)}")
print(f"Число {number_3}: {numbersss(number_3)}")

