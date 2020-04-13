# Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random


SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]
print(*matrix, sep='\n')

max_in_min = -1
for line in matrix:
    min_in_line = 0
    for i in line:
        if i > min_in_line:
            min_in_line = i
    for i in line:
        if i <= min_in_line:
            min_in_line = i
    if min_in_line > max_in_min:
        max_in_min = min_in_line

print(f'Максимальный элемент среди минимальных это {max_in_min}')


