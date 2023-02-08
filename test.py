from math import sqrt


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Выводит на экран значение квадратного корня."""
    if your_number <= 0:
        return
    value = calculate_square_root(your_number)
    print((f'Мы вычислили квадратный корень из введённого вами числа.'
           f' Это будет: {value}'))


message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)
print(message)
calc(25.5)
