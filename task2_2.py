class HexNumber:

    def __init__(self, number):
        self.number = list(str(number))

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return HexNumber(hex(int(''.join(self.number), 16) + int(''.join(other.number), 16))[2:])

    def __mul__(self, other):
        return HexNumber(hex(int(''.join(self.number), 16) * int(''.join(other.number), 16))[2:])


def hex_input(txt):
    num = input(txt)
    try:
        int(num, 16)
        return num
    except ValueError:
        return hex_input(txt)


first = hex_input('Введите первое шестнадцатиричное число: ')
second = hex_input('Введите второе шестнадцатиричное число: ')
print(f'Сумма чисел равна: {HexNumber(first) + HexNumber(second)}')
print(f'Произведение чисел равно: {HexNumber(first) * HexNumber(second)}')