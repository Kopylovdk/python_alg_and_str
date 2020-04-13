# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random

SIZE = 10  # Для 10_000_000 работает около 9-10 секунд.
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Диапазон {array}')


i = 0
max_index = -1
for i in range(len(array)):
    if array[i] < 0 and max_index == -1:
        max_index = i
    elif 0 > array[i] > array[max_index]:
        max_index = i
if max_index == -1:
    print('Отрицательных элементов в массиве нет.')
else:
    print(f'Максимальное отрицательное значение = {array[max_index]}, его позиция {max_index + 1}')
