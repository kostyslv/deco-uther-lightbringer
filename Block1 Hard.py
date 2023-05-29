"""Функция возвращает сумму обязательных аргументов, первых двух позиционных и одного случайного переданного по значению"""
import random


def summarize(num1, num2, *args, **kwargs):
    return num1 + num2 + args[0] + args[1] + random.choice(list(kwargs.values()))


print(summarize(1, 2, 3, 4, 6, 8, 10, num3=10, num4=11))
