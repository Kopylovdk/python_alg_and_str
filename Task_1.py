# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
from sys import getsizeof
import random
import copy


def show(x):
    print(f'type={type(x)}, size={getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)


array = [random.randint(-10, 10) for _ in range(10)]     # 92 + 140, если 0 в "array" + 138
# print('*' * 50)
# print('Вариант 1')
n_old = copy.copy(array)   # 68 + 140, , если 0 в "array" + 138
min_n = min(array)  # 14
max_n = max(array)  # 14
ind_min = array.index(min_n)  # 14
ind_max = array.index(max_n)  # 14
spam = array[ind_min]  # 14
array[ind_min] = array[ind_max]  # 14
array[ind_max] = spam  # 14
# 68 + 140 + 92 + 140 + 14 + 14 + 14 + 14 + 14 + 14 + 14 = 538

# print('*' * 50)
# print('Вариант 2')
n_min = 0  # 12, после выполнения цикла будет 14 (если будет 0 - то останется 12)
n_max = 0  # 12, после выполнения цикла будет 14 (если будет 0 - то останется 12)
n_old = copy.copy(array)  # 68 + 140, , если 0 в "array" + 138
for i in range(len(array)):  # 14
    if array[i] < array[n_min]:
        n_min = i
    elif array[i] > array[n_max]:
        n_max = i
spam = array[n_min]  # 14
array[n_min] = array[n_max]  # 14
array[n_max] = spam  # 14
# 92 + 140 + 14 + 14 + 68 + 140 + 14 + 14 + 14 + 14 = 524

# print('*' * 50)
# print('Вариант 3')
spam = sorted(array)  # 96 + 140, если 0 в "array" + 138
n_min = spam[0]  # 14
n_max = spam[-1]  # 14
n_new = copy.copy(array)  # 68 + 140, , если 0 в "array" + 138
ind_min = n_new.index(n_min)  # 14
ind_max = n_new.index(n_max)  # 14
eggs = n_new[ind_min]  # 14
n_new[ind_min] = n_new[ind_max]  # 14
n_new[ind_max] = eggs  # 14
# 92 + 96 + 280 + 28 + 68 + 140 + 70 = 774

# Вариант 1 - 538
# Вариант 2 - 524
# Вариант 3 - 774

# Я считал с помощью функции написанной на уроке).
# Во всех вариантах, если переменная получит значение 0 - то размер будет 12,
# далее до 32767 размер будет 14, он и учитывался в подсчете.
# Выводы:
# Во варианте 2, по сравнению в вариантом 1, используется меньшее количетво переменных.
# Т.е. Вариант 2 легче Варианта 1 на вес двух переменных, НО т.к. во варианте 2 присутствует цикл,
# i которого по размеру == размеру одной из двух переменных варианта 1, поэтому разница в размере одной переменной.
# Во варианте 3, по сравнению с вариантом 1, используется на одну копию массива больше, причем отсортированного,
# а по сравнению с вариантом 2 еще и на одну переменную больше.
# Из выводов выше следует, что вариант 2 поедает меньше памяти.
#
# операционная система x64
# print(platform.python_implementation())
# CPython
# print(platform.architecture())CPython
# ('32bit', 'WindowsPE')
