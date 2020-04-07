# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
number_counts = 0      # Если я не объявляю переменную, то пайчарм говорит, что она возможно не объявлена....
while True:
    try:
        number_counts = int(input('Введите количество чисел, которые вы хотите проверить: '))
        break
    except ValueError:
        print('Вы ввели не целое число. Повторите ввод!')
        continue
number_search = 0    # Если я не объявляю переменную, то пайчарм говорит, что она возможно не объявлена....
while True:
    try:
        number_search = int(input('Введите цифру, которое вы хотите искать: '))
        break
    except ValueError:
        print('Вы ввели не целое число. Повторите ввод!')
        continue
a = 0
number_count_in = 0
while a < number_counts:
    number = 0
    while True:
        try:
            number = int(input('Введите целое число: '))
            break
        except ValueError:
            print('Вы ввели не целое число. Повторите ввод!')
            continue
    while True:
        if number % 10 == number_search:
            number_count_in += 1
        if number // 10 == 0:
            break
        number = number // 10
    a += 1
print(f'Цифра {number_search} встречается {number_count_in}')
