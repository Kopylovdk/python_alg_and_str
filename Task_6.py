# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Диапазон {array}')

# Находим индекс минимального значения и максимального значения
array_min = 0
array_max = 0
for i in range(len(array)):
    if array[i] < array[array_min]:
        array_min = i
    elif array[i] > array[array_max]:
        array_max = i
print(f'Минимальное значение с индексом {array_min} = {array[array_min]}\n'
      f'Максимальное значение с индексом {array_max} = {array[array_max]}\n')

sum_values = 0
if array_min > array_max:
    for i in range(array_max + 1, array_min):
        sum_values = sum_values + array[i]
else:
    for i in range(array_min + 1, array_max):
        sum_values = sum_values + array[i]
if sum_values == 0:
    print('Между минимальным и максимальным числом в массиве нет записей.')
else:
    print(f'Сумма элементов массива между минимальным и максимальным занчениями = {sum_values}')
