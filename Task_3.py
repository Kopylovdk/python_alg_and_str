# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
import random


def my_median(arr, pivot_fn=random.choice):
    if len(arr) % 2 == 1:
        return my_select(arr, len(arr) / 2, pivot_fn)
    else:
        return 0.5 * (my_select(arr, len(arr) / 2 - 1, pivot_fn) +
                      my_select(arr, len(arr) / 2, pivot_fn))


def my_select(arr, idx, pivot_fn):
    if len(arr) == 1:
        return arr[0]
    pivot = pivot_fn(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    if idx < len(lows):
        return my_select(lows, idx, pivot_fn)
    elif idx < len(lows) + len(pivots):
        return pivots[0]
    else:
        return my_select(highs, idx - len(lows) - len(pivots), pivot_fn)


SIZE = 5
array = [random.randint(0, 100) for _ in range(2 * SIZE + 1)]
print(array)
# print(sorted(array))  # для проверки
print(my_median(array))
