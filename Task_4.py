# Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Диапазон {array}')

max_num = array[0]
max_count = 1
for i in range(len(array) - 1):
    count = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            count += 1
    if count > max_count:
        max_count = count
        max_num = array[i]

if max_count > 1:
    print(f'{max_count} раз(а) встречается число {max_num}')
else:
    print('Все элементы уникальны')
