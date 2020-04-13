# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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
print(f'Минимальное значение = {array[array_min]}\nМаксимальное значение = {array[array_max]}')

# меняем местами используя временную переменную
spam_number = array[array_min]
array[array_min] = array[array_max]
array[array_max] = spam_number
print(f'Минимальное и максимальное значение поменяны местами {array}')
