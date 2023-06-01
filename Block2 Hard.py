"""Перенести счетчик на уровень глобальной функции. Чтобы функция заработала прокидываю
count в параметр функции суммирования"""
def call_summarize():
    count = 0
    summa = summarize(3, 6, count)
    return summa


def summarize(num1, num2, count):
    count += 1
    print(f'Функция вызвана: {count} раз')
    return num1 + num2


result = call_summarize()
print(result)
