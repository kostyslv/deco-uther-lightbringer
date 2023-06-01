count = 0


def func0():
    global count
    count += 1
    print(f'Вызвана функция {func0.__name__}, счетчик вызова функций {count}')


def func1():
    global count
    count += 1
    print(f'Вызвана функция {func1.__name__}, счетчик вызова функций {count}')


def func2():
    global count
    count += 1
    print(f'Вызвана функция {func2.__name__}, счетчик вызова функций {count}')


def call_summarize():
    summa = summarize(3, 6)
    return summa


def summarize(num1, num2):
    global count
    count += 1
    print(f'Функция вызвана: {count} раз')
    return num1 + num2


func0()
summarize(1, 3)
func1()
summarize(2, 7)
func2()
summarize(5, 3)
result = call_summarize()
print(result)
res = call_summarize # Реалезация 4 пункта, не совсем понял задание, из какой переменной осуществлять вызов
print(res())