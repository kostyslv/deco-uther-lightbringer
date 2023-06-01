count = 0

def summarize(num1, num2):
    global count
    count += 1
    print(f'Функция вызвана: {count} раз')
    return num1 + num2

summarize(1, 3)
summarize(2, 7)
summarize(5, 3)