# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a = float(input('Введите число a: '))
b = float(input('Введите число b: '))
c = float(input('Введите число c: '))

if a > b:
    if a > c:
        if b > c:
            print(f'Среднее число b = {b}')
        else:
            print(f'Среднее число c = {c}')
    else:
        print(f'Среднее число a = {a}')
else:
    if b > c:
        if c > a:
            print(f'Среднее число c = {c}')
        else:
            print(f'Среднее число a = {a}')
    else:
        print(f'Среднее число b = {b}')
