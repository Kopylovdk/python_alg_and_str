# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
import random


#  Сортировка пузырьком по возрастанию
def bubble_sort(arr):
    while True:
        spam = 0
        for i in range(len(arr) - 1):
            j = len(arr) - i - 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                spam += 1
        if spam == 0:
            break


#  Сортировка пузырьком по убыванию
def bubble_sort_desc(arr):
    while True:
        spam = 0
        for i in range(len(arr) - 1):
            j = len(arr) - i - 1
            if arr[j] > arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                spam += 1
        if spam == 0:
            break


SIZE = 10
array = [random.randint(-100, 99) for _ in range(SIZE)]

print('Исходный порядок:\n', array)
bubble_sort(array)
print('По возрастанию:\n', array)
bubble_sort_desc(array)
print('По убыванию:\n', array)
