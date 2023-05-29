def summarize_1(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print(summarize_1(1, 2))
print(summarize_1(3, 4, 7, 12))
print(summarize_1(3, 4, 7, 12, num1=0, num2=5))


def summarize_2(num1, num2, num3, num4, *args, **kwargs):
    return num1 + num2 + num3 + num4 + sum(args) + sum(kwargs.values())


print(summarize_2(1, 2, 4, 5, 6, 7, 8, 10))  # ошибки нет
print(summarize_2(1))  # один аргумент, ошибка
print(summarize_2(1, 3, 5, 6, num1=2))  # обязательный аргумент одновременно передается позиционно и по ключу, ошибка
param_tuple = (1, 2, 3, 4, 5)
print(summarize_2(*param_tuple))  # распаковать кортеж
param_dict = {'num1': 8, 'num2': 5, 'num3': 7, 'num4': 3}
print(summarize_2(*param_dict))  # ошибка при распаковке словаря
print(summarize_2(**param_dict))  # распаковка словаря
