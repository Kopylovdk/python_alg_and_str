# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Диапазон {array}')

array_min = 0
array_min_2 = 0

if array[0] > array[1]:
    array_min = 0
    array_min_2 = 1
else:
    array_min = 1
    array_min_2 = 0

for i in range(2, len(array)):
    if array[i] < array[array_min]:
        spam_number = array_min
        array_min = i
        if array[spam_number] < array[array_min_2]:
            array_min_2 = spam_number
    elif array[i] < array[array_min_2]:
        array_min_2 = i

print(f'Первый наименьший элемент = {array[array_min]}\n'
      f'Второй наименьший элемент = {array[array_min_2]}\n')
