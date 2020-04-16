import random
import timeit
import cProfile
import copy


print('Вариант 1')


def min_max_alg(size):
    n = [random.randint(-1000, 1000) for _ in range(size)]
    n_min = 0
    n_max = 0
    n_old = copy.copy(n)
    for i in range(len(n)):
        if n[i] < n[n_min]:
            n_min = i
        elif n[i] > n[n_max]:
            n_max = i
    n[n_min], n[n_max] = n[n_max], n[n_min]
    return f'Оригинальная последовательность\n{n_old}\n' \
           f'Минимальное значение = {n[n_min]}\nМаксимальное значение = {n[n_max]}\n' \
           f'Минимальное и максимальное значение поменяны местами: {n}\n'


# print(timeit.timeit('min_max_alg(10000)', number=1000, globals=globals()))  # 11.228229800000001
# print(timeit.timeit('min_max_alg(20000)', number=1000, globals=globals()))  # 22.5124038
# print(timeit.timeit('min_max_alg(30000)', number=1000, globals=globals()))  # 33.5169278
# print(timeit.timeit('min_max_alg(40000)', number=1000, globals=globals()))  # 44.711330000000004
# print(timeit.timeit('min_max_alg(50000)', number=1000, globals=globals()))  # 55.90590510000001
# print(timeit.timeit('min_max_alg(60000)', number=1000, globals=globals()))  # 66.87875779999999
# print(timeit.timeit('min_max_alg(70000)', number=1000, globals=globals()))  # 78.19096240000002
# print(timeit.timeit('min_max_alg(80000)', number=1000, globals=globals()))  # 89.18070069999999
# print(timeit.timeit('min_max_alg(90000)', number=1000, globals=globals()))  # 100.13837889999996
# print(timeit.timeit('min_max_alg(100000)', number=1000, globals=globals()))  # 111.22605489999995
# print(timeit.timeit('min_max_alg(110000)', number=1000, globals=globals()))  # 122.42083830000001
# print(timeit.timeit('min_max_alg(120000)', number=1000, globals=globals()))  # 133.8020772000001
# print(timeit.timeit('min_max_alg(130000)', number=1000, globals=globals()))  # 145.08420239999998
# print(timeit.timeit('min_max_alg(140000)', number=1000, globals=globals()))  # 156.35570310000003
#
# cProfile.run('min_max_alg(10000)')  # 1    0.004    0.004    0.020    0.020 Task_1.py:8(min_max_alg)
# cProfile.run('min_max_alg(20000)')  # 1    0.007    0.007    0.041    0.020 Task_1.py:8(min_max_alg)
# cProfile.run('min_max_alg(30000)')  # 1    0.011    0.011    0.061    0.061 Task_1.py:8(min_max_alg)
# cProfile.run('min_max_alg(40000)')  # 1    0.015    0.015    0.081    0.081 Task_1.py:8(min_max_alg)
# cProfile.run('min_max_alg(50000)')  # 1    0.018    0.018    0.104    0.104 Task_1.py:8(min_max_alg)
# cProfile.run('min_max_alg(60000)')  # 1    0.021    0.021    0.121    0.121 Task_1.py:8(min_max_alg)
# cProfile.run('min_max_alg(70000)')  # 1    0.024    0.024    0.144    0.144 Task_1.py:8(min_max_alg)
# cProfile.run('min_max_alg(80000)')  # 1    0.028    0.028    0.164    0.164 Task_1.py:8(min_max_alg)
# cProfile.run('min_max_alg(90000)')  # 1    0.031    0.031    0.180    0.180 Task_1.py:8(min_max_alg)
# cProfile.run('min_max_alg(100000)')  # 1    0.034    0.034    0.205    0.205 Task_1.py:8(min_max_alg)
# cProfile.run('min_max_alg(110000)')  # 1    0.039    0.039    0.222    0.222 Task_1.py:8(min_max_alg)
# cProfile.run('min_max_alg(120000)')  # 1    0.042    0.042    0.245    0.245 Task_1.py:8(min_max_alg)
# cProfile.run('min_max_alg(130000)')  # 1    0.046    0.046    0.264    0.264 Task_1.py:8(min_max_alg)
# cProfile.run('min_max_alg(140000)')  # 1    0.050    0.050    0.288    0.288 Task_1.py:8(min_max_alg)

print('*' * 50)
print('Вариант 2. Встроенные функции min / max')


def min_max_py(size):
    n = [random.randint(-1000, 1000) for _ in range(size)]
    n_old = copy.copy(n)
    min_n = min(n)
    max_n = max(n)
    ind_min, ind_max = n.index(min_n), n.index(max_n)
    n[ind_min], n[ind_max] = n[ind_max], n[ind_min]
    return f'Оригинальная последовательность\n{n_old}\n' \
           f'Минимальное значение = {min_n}\nМаксимальное значение = {max_n}\n' \
           f'Минимальное и максимальное значение поменяны местами:\n{n}'


# print('Для сравнения с вариантом 4.')
# print(timeit.timeit('min_max_py(100)', number=1000, globals=globals()))  # 0.103076
# print(timeit.timeit('min_max_py(200)', number=1000, globals=globals()))  # 0.20225959999999998
# print(timeit.timeit('min_max_py(300)', number=1000, globals=globals()))  # 0.3034575
# print(timeit.timeit('min_max_py(400)', number=1000, globals=globals()))  # 0.40047959999999994
# print(timeit.timeit('min_max_py(500)', number=1000, globals=globals()))  # 0.5012083
# print(timeit.timeit('min_max_py(600)', number=1000, globals=globals()))  # 0.6005456
# print(timeit.timeit('min_max_py(700)', number=1000, globals=globals()))  # 0.6939721999999997
# print(timeit.timeit('min_max_py(800)', number=1000, globals=globals()))  # 0.7957964999999998
# print(timeit.timeit('min_max_py(900)', number=1000, globals=globals()))  # 0.8951097000000003
# print(timeit.timeit('min_max_py(1000)', number=1000, globals=globals()))  # 0.9934978000000001
# print(timeit.timeit('min_max_py(1100)', number=1000, globals=globals()))  # 1.0898086999999999
# print(timeit.timeit('min_max_py(1200)', number=1000, globals=globals()))  # 1.2156330999999998
# print(timeit.timeit('min_max_py(1300)', number=1000, globals=globals()))  # 1.3282103000000003
# print(timeit.timeit('min_max_py(1400)', number=1000, globals=globals()))  # 1.3938477000000002

# print('Для сравнения с вариантами 1 и 3.')
# print(timeit.timeit('min_max_py(10000)', number=1000, globals=globals()))  # 9.89370299999996
# print(timeit.timeit('min_max_py(20000)', number=1000, globals=globals()))  # 19.600484599999845
# print(timeit.timeit('min_max_py(30000)', number=1000, globals=globals()))  # 29.504747499999894
# print(timeit.timeit('min_max_py(40000)', number=1000, globals=globals()))  # 39.27861299999995
# print(timeit.timeit('min_max_py(50000)', number=1000, globals=globals()))  # 49.25770089999992
# print(timeit.timeit('min_max_py(60000)', number=1000, globals=globals()))  # 59.15819310000006
# print(timeit.timeit('min_max_py(70000)', number=1000, globals=globals()))  # 68.9984892
# print(timeit.timeit('min_max_py(80000)', number=1000, globals=globals()))  # 78.83509640000011
# print(timeit.timeit('min_max_py(90000)', number=1000, globals=globals()))  # 88.54663659999983
# print(timeit.timeit('min_max_py(100000)', number=1000, globals=globals()))  # 98.4843598
# print(timeit.timeit('min_max_py(110000)', number=1000, globals=globals()))  # 108.65346840000007
# print(timeit.timeit('min_max_py(120000)', number=1000, globals=globals()))  # 118.62715079999998
# print(timeit.timeit('min_max_py(130000)', number=1000, globals=globals()))  # 128.52782119999983
# print(timeit.timeit('min_max_py(140000)', number=1000, globals=globals()))  # 138.73468550000007
#
# cProfile.run('min_max_py(10000)')  # 1    0.002    0.002    0.019    0.019 Task_1.py:58(min_max_py)
# cProfile.run('min_max_py(20000)')  # 1    0.003    0.003    0.038    0.038 Task_1.py:58(min_max_py)
# cProfile.run('min_max_py(30000)')  # 1    0.005    0.005    0.057    0.057 Task_1.py:58(min_max_py)
# cProfile.run('min_max_py(40000)')  # 1    0.007    0.007    0.075    0.075 Task_1.py:58(min_max_py)
# cProfile.run('min_max_py(50000)')  # 1    0.009    0.009    0.097    0.097 Task_1.py:58(min_max_py)
# cProfile.run('min_max_py(60000)')  # 1    0.011    0.011    0.114    0.114 Task_1.py:58(min_max_py)
# cProfile.run('min_max_py(70000)')  # 1    0.013    0.013    0.134    0.134 Task_1.py:58(min_max_py)
# cProfile.run('min_max_py(80000)')  # 1    0.014    0.014    0.152    0.152 Task_1.py:58(min_max_py)
# cProfile.run('min_max_py(90000)')  # 1    0.016    0.016    0.173    0.173 Task_1.py:58(min_max_py)
# cProfile.run('min_max_py(100000)')  # 1    0.019    0.019    0.189    0.189 Task_1.py:58(min_max_py)
# cProfile.run('min_max_py(110000)')  # 1    0.020    0.020    0.212    0.212 Task_1.py:58(min_max_py)
# cProfile.run('min_max_py(120000)')  # 1    0.022    0.022    0.227    0.227 Task_1.py:58(min_max_py)
# cProfile.run('min_max_py(130000)')  # 1    0.024    0.024    0.249    0.249 Task_1.py:58(min_max_py)
# cProfile.run('min_max_py(140000)')  # 1    0.026    0.026    0.269    0.269 Task_1.py:58(min_max_py)

print('*' * 50)
print('Вариант 3. Встроенная функция sorted')


def min_max_sort(size):
    n = [random.randint(-1000, 1000) for _ in range(size)]
    spam = sorted(n)
    n_min = spam[0]
    n_max = spam[-1]
    n_new = copy.copy(n)
    ind_min, ind_max = n_new.index(n_min), n_new.index(n_max)
    n_new[ind_min], n_new[ind_max] = n_new[ind_max], n_new[ind_min]
    return f'Оригинальная последовательность\n{n}\n' \
           f'Минимальное значение = {n_min}\nМаксимальное значение = {n_max}\n' \
           f'Минимальное и максимальное значение поменяны местами:\n {n_new}'


# print(timeit.timeit('min_max_sort(10000)', number=1000, globals=globals()))  # 10.617288700000245
# print(timeit.timeit('min_max_sort(20000)', number=1000, globals=globals()))  # 21.44600730000002
# print(timeit.timeit('min_max_sort(30000)', number=1000, globals=globals()))  # 31.953487199999927
# print(timeit.timeit('min_max_sort(40000)', number=1000, globals=globals()))  # 42.93176390000008
# print(timeit.timeit('min_max_sort(50000)', number=1000, globals=globals()))  # 53.56146949999993
# print(timeit.timeit('min_max_sort(60000)', number=1000, globals=globals()))  # 64.43872069999998
# print(timeit.timeit('min_max_sort(70000)', number=1000, globals=globals()))  # 75.49533379999957
# print(timeit.timeit('min_max_sort(80000)', number=1000, globals=globals()))  # 86.3846954999999
# print(timeit.timeit('min_max_sort(90000)', number=1000, globals=globals()))  # 96.93117080000002
# print(timeit.timeit('min_max_sort(100000)', number=1000, globals=globals()))  # 107.77210080000032
# print(timeit.timeit('min_max_sort(110000)', number=1000, globals=globals()))  # 119.0629984000002
# print(timeit.timeit('min_max_sort(120000)', number=1000, globals=globals()))  # 129.61085939999975
# print(timeit.timeit('min_max_sort(130000)', number=1000, globals=globals()))  # 141.82776560000002
# print(timeit.timeit('min_max_sort(140000)', number=1000, globals=globals()))  # 151.81482689999984
#
# cProfile.run('min_max_sort(10000)')  # 1    0.002    0.002    0.019    0.019 Task_1.py:105(min_max_sort)
# cProfile.run('min_max_sort(20000)')  # 1    0.003    0.003    0.039    0.039 Task_1.py:105(min_max_sort)
# cProfile.run('min_max_sort(30000)')  # 1    0.005    0.005    0.059    0.059 Task_1.py:105(min_max_sort)
# cProfile.run('min_max_sort(40000)')  # 1    0.007    0.007    0.079    0.079 Task_1.py:105(min_max_sort)
# cProfile.run('min_max_sort(50000)')  # 1    0.009    0.009    0.102    0.102 Task_1.py:105(min_max_sort)
# cProfile.run('min_max_sort(60000)')  # 1    0.011    0.011    0.118    0.118 Task_1.py:105(min_max_sort)
# cProfile.run('min_max_sort(70000)')  # 1    0.013    0.013    0.140    0.140 Task_1.py:105(min_max_sort)
# cProfile.run('min_max_sort(80000)')  # 1    0.014    0.014    0.159    0.159 Task_1.py:105(min_max_sort)
# cProfile.run('min_max_sort(90000)')  # 1    0.016    0.016    0.179    0.179 Task_1.py:105(min_max_sort)
# cProfile.run('min_max_sort(100000)')  # 1    0.018    0.018    0.197    0.197 Task_1.py:105(min_max_sort)
# cProfile.run('min_max_sort(110000)')  # 1    0.021    0.021    0.222    0.222 Task_1.py:105(min_max_sort)
# cProfile.run('min_max_sort(120000)')  # 1    0.022    0.022    0.238    0.238 Task_1.py:105(min_max_sort)
# cProfile.run('min_max_sort(130000)')  # 1    0.023    0.023    0.261    0.261 Task_1.py:105(min_max_sort)
# cProfile.run('min_max_sort(140000)')  # 1    0.028    0.028    0.288    0.288 Task_1.py:105(min_max_sort)

print('*' * 50)
print('Вариант 4. Такой же, как и вариант 3, но сортировка в функции.')


def min_max_my_sort(size):
    def _my_sort(array):
        for i in range(len(array) - 1, 0, -1):
            for j in range(i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array

    n = [random.randint(-1000, 1000) for _ in range(size)]
    n_new = copy.copy(n)
    n_old = copy.copy(n)
    n = _my_sort(n)
    n_min = n[0]
    n_max = n[-1]
    ind_min, ind_max = n_new.index(n_min), n_new.index(n_max)
    n_new[ind_min], n_new[ind_max] = n_new[ind_max], n_new[ind_min]
    return f'Оригинальная последовательность\n{n_old}\n' \
           f'Минимальное значение = {n_min}\nМаксимальное значение = {n_max}\n' \
           f'Минимальное и максимальное значение поменяны местами:\n {n_new}'


# # для size = 10_000 - 9917.2277953, для 20_000 работало больше 8 часов, но результата не было.
# print(timeit.timeit('min_max_my_sort(100)', number=11000, globals=globals()))  # 1.0484128000000001
# print(timeit.timeit('min_max_my_sort(200)', number=1000, globals=globals()))  # 3.8686605
# print(timeit.timeit('min_max_my_sort(300)', number=1000, globals=globals()))  # 8.5905555
# print(timeit.timeit('min_max_my_sort(400)', number=1000, globals=globals()))  # 15.499230499999998
# print(timeit.timeit('min_max_my_sort(500)', number=1000, globals=globals()))  # 24.2610168
# print(timeit.timeit('min_max_my_sort(600)', number=1000, globals=globals()))  # 34.76117
# print(timeit.timeit('min_max_my_sort(700)', number=1000, globals=globals()))  # 48.199894400000005
# print(timeit.timeit('min_max_my_sort(800)', number=1000, globals=globals()))  # 62.407223999999985
# print(timeit.timeit('min_max_my_sort(900)', number=1000, globals=globals()))  # 80.70949580000001
# print(timeit.timeit('min_max_my_sort(1000)', number=1000, globals=globals()))  # 98.20890760000003
# print(timeit.timeit('min_max_my_sort(1100)', number=1000, globals=globals()))  # 119.65068120000001
# print(timeit.timeit('min_max_my_sort(1200)', number=1000, globals=globals()))  # 141.1575077
# print(timeit.timeit('min_max_my_sort(1300)', number=1000, globals=globals()))  # 169.7929289
# print(timeit.timeit('min_max_my_sort(1400)', number=1000, globals=globals()))  # 193.29759609999996
#
# cProfile.run('min_max_my_sort(100)')  # 1    0.001    0.001    0.001    0.001 Task_1.py:153(_my_sort)
# cProfile.run('min_max_my_sort(200)')  # 1    0.004    0.004    0.004    0.004 Task_1.py:153(_my_sort)
# cProfile.run('min_max_my_sort(300)')  # 1    0.008    0.008    0.008    0.008 Task_1.py:153(_my_sort)
# cProfile.run('min_max_my_sort(400)')  # 1    0.016    0.016    0.016    0.016 Task_1.py:153(_my_sort)
# cProfile.run('min_max_my_sort(500)')  # 1    0.024    0.024    0.024    0.024 Task_1.py:153(_my_sort)
# cProfile.run('min_max_my_sort(600)')  # 1    0.034    0.034    0.034    0.034 Task_1.py:153(_my_sort)
# cProfile.run('min_max_my_sort(700)')  # 1    0.047    0.047    0.047    0.047 Task_1.py:153(_my_sort)
# cProfile.run('min_max_my_sort(800)')  # 1    0.062    0.062    0.062    0.062 Task_1.py:153(_my_sort)
# cProfile.run('min_max_my_sort(900)')  # 1    0.080    0.080    0.080    0.080 Task_1.py:153(_my_sort)
# cProfile.run('min_max_my_sort(1000)')  # 1    0.100    0.100    0.100    0.100 Task_1.py:153(_my_sort)
# cProfile.run('min_max_my_sort(1100)')  # 1    0.121    0.121    0.121    0.121 Task_1.py:153(_my_sort)
# cProfile.run('min_max_my_sort(1200)')  # 1    0.142    0.142    0.142    0.142 Task_1.py:153(_my_sort)
# cProfile.run('min_max_my_sort(1300)')  # 1    0.167    0.167    0.167    0.167 Task_1.py:153(_my_sort)
# cProfile.run('min_max_my_sort(1400)')  # 1    0.194    0.194    0.194    0.194 Task_1.py:153(_my_sort)


# Выводы:
#    Замеры для вариантов 1 и 3 проводились для n = 10_000 с шагом 10_000
#    Замеры для варианта 2 проводились для n = 10_000 с шагом 10_000 и n = 100 с шагом 100
#    Замеры для варианта 4 проводились для n = 100 с шагом 100
# 1. Варианты 1, 2, 3 - имют линейные зависимости
# 2. Вариант 4 - квадратичную зависимость
# 3. Графики приложил по ссылке в Google.docs.
# https://docs.google.com/spreadsheets/d/1ZSBQD_MjyWAE-CGkUSAQr2QdFX2gDUzP7sX_6HNggTw/edit?usp=sharing
#    Там наглядно видно, что Вариант 2 работает быстрее чем 3 и 1.
# 4. После сравнения Варианта 2 с Вариантом 4, на данных одинакового объема, также наглядно видна разница.
# 5. В Варианте 4 самым слабым местом является функция сортировки - _my_sort().
#    Она явно проигрывает встроенной функции sorted() из Варианта 3.
# 6. Самым быстрым способом оказался Вариант 2, в котором используются встроенные функции min() и max()
#    для поиска минимального и максимального значения. Во Варианте 2 по сравнению с вариантом 3 на одну операцию меньше,
#    по сравнению с вариантами 1 и 4, то во варианте 2 отсутствуют циклы.
