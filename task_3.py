# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.


def reverse(a):
    if a // 10 == 0:
        return a
    else:
        b = a % 10
        a = a // 10
        return f'{b}{reverse(a)}'


number = 0     # Если я не объявляю переменную, то пайчарм говорит, что она возможно не объявлена....
while True:
    try:
        number = int(input('Введите целое число: '))
        break
    except ValueError:
        print('Вы ввели не целое число. Повторите ввод!')
        continue
# В этом случае, при вводе 100500 вернется 5001 в виде класса int.
print(f'Вы ввели {number}\n'
      f'Обратное по поряку: {int(reverse(number))}')
# В этом случае, при вводе 100500 вернется 005001 в виде класса str.
# print(f'Вы ввели {number}\n'
#       f'Обратное по поряку: {reverse(number)}')
