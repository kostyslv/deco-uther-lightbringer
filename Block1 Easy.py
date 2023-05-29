def print_text(text: str, amount: int) -> str:
    string = text
    while amount > 1:
        if amount % 2 == 0:
            string += text.lower()
        else:
            string += text.upper()
        amount -= 1

    return string


test_func = print_text(text='test', amount=3)
print(test_func)
