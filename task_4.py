# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
turn = 0      # Если я не объявляю переменную, то пайчарм говорит, что она возможно не объявлена....
while True:
    try:
        turn = int(input('Введите количество элементов ряда для сложения: '))
        break
    except ValueError:
        print('Вы ввели не целое число. Повторите ввод!')
        continue
n = 0
first = 1
result = 0
while n < turn:
    n += 1
    result = result + first
    first = first / 2 * -1
print(result)
