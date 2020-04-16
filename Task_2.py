import timeit
import cProfile


def eratosthenes_sieve(n):
    cnt = 1
    start = 3
    stop = 4 * n
    sieve = [i for i in range(start, stop) if i % 2 != 0]
    prime = [2]
    if n == 1:
        return 2
    while cnt < n:
        for i in range(len(sieve)):
            if sieve[i] != 0:
                cnt += 1
                if cnt == n:
                    return sieve[i]
                j = i + sieve[i]
                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]
        prime.extend([i for i in sieve if i != 0])
        start, stop = stop, stop + 2 * n
        sieve = [i for i in range(start, stop) if i % 2 != 0]
        for i in range(len(sieve)):
            for j in prime:
                if sieve[i] % j == 0:
                    sieve[i] = 0
                    break


def my_prime(n):
    i = 1
    number = 1
    prime = [2]
    if n == 1:
        return 2
    while i != n:
        number += 2
        for j in prime:
            if number % j == 0:
                break
        else:
            i += 1
            prime.append(number)
    return number


print('* Решето ' * 15)
# print(timeit.timeit('eratosthenes_sieve(100)', number=1000, globals=globals()))  # 0.2863742
# print(timeit.timeit('eratosthenes_sieve(200)', number=1000, globals=globals()))  # 1.6441911999999999
# print(timeit.timeit('eratosthenes_sieve(300)', number=1000, globals=globals()))  # 3.2212981000000003
# print(timeit.timeit('eratosthenes_sieve(400)', number=1000, globals=globals()))  # 5.051961299999999
# print(timeit.timeit('eratosthenes_sieve(500)', number=1000, globals=globals()))  # 7.403153
# print(timeit.timeit('eratosthenes_sieve(600)', number=1000, globals=globals()))  # 10.121970999999998
# print(timeit.timeit('eratosthenes_sieve(700)', number=1000, globals=globals()))  # 13.129537199999998
# print(timeit.timeit('eratosthenes_sieve(800)', number=1000, globals=globals()))  # 16.929592900000003
# print(timeit.timeit('eratosthenes_sieve(900)', number=1000, globals=globals()))  # 20.3663258
# print(timeit.timeit('eratosthenes_sieve(1000)', number=1000, globals=globals()))  # 24.334263000000007
# print(timeit.timeit('eratosthenes_sieve(1100)', number=1000, globals=globals()))  # 48.655623099999985
# print(timeit.timeit('eratosthenes_sieve(1200)', number=1000, globals=globals()))  # 56.211433400000004
# print(timeit.timeit('eratosthenes_sieve(1300)', number=1000, globals=globals()))  # 65.08952140000002
# print(timeit.timeit('eratosthenes_sieve(1400)', number=1000, globals=globals()))  # 74.08000299999998
# print(timeit.timeit('eratosthenes_sieve(1500)', number=1000, globals=globals()))  # 84.98277389999998

# print(timeit.timeit('eratosthenes_sieve(1000)', number=1000, globals=globals()))  # 24.025684199999997
# print(timeit.timeit('eratosthenes_sieve(2000)', number=1000, globals=globals()))  # 138.71045679999997
# print(timeit.timeit('eratosthenes_sieve(3000)', number=1000, globals=globals()))  # 281.502207
# print(timeit.timeit('eratosthenes_sieve(4000)', number=1000, globals=globals()))  # 548.0257431
# print(timeit.timeit('eratosthenes_sieve(5000)', number=1000, globals=globals()))  # 915.557943
# print(timeit.timeit('eratosthenes_sieve(6000)', number=1000, globals=globals()))  # 1353.6691648999997


cProfile.run('eratosthenes_sieve(100)')  #

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Task_2.py:23(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Task_2.py:25(<listcomp>)
#         1    0.000    0.000    0.000    0.000 Task_2.py:5(eratosthenes_sieve)
#         1    0.000    0.000    0.000    0.000 Task_2.py:9(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       345    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}

cProfile.run('eratosthenes_sieve(1000)')  #

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.024    0.024 <string>:1(<module>)
#         2    0.000    0.000    0.000    0.000 Task_2.py:23(<listcomp>)
#         2    0.000    0.000    0.000    0.000 Task_2.py:25(<listcomp>)
#         1    0.024    0.024    0.024    0.024 Task_2.py:5(eratosthenes_sieve)
#         1    0.000    0.000    0.000    0.000 Task_2.py:9(<listcomp>)
#         1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
#      4278    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}

cProfile.run('eratosthenes_sieve(5000)')  #

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.916    0.916 <string>:1(<module>)
#         3    0.001    0.000    0.001    0.000 Task_2.py:23(<listcomp>)
#         3    0.002    0.001    0.002    0.001 Task_2.py:25(<listcomp>)
#         1    0.910    0.910    0.916    0.916 Task_2.py:5(eratosthenes_sieve)
#         1    0.001    0.001    0.001    0.001 Task_2.py:9(<listcomp>)
#         1    0.000    0.000    0.916    0.916 {built-in method builtins.exec}
#     23570    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}

print()
print('* Мое простое ' * 10)
# print(timeit.timeit('my_prime(100)', number=1000, globals=globals()))  # 0.2679455999999618
# print(timeit.timeit('my_prime(200)', number=1000, globals=globals()))  # 1.018420400000025
# print(timeit.timeit('my_prime(300)', number=1000, globals=globals()))  # 2.2863150999999675
# print(timeit.timeit('my_prime(400)', number=1000, globals=globals()))  # 4.056229900000005
# print(timeit.timeit('my_prime(500)', number=1000, globals=globals()))  # 6.367885100000024
# print(timeit.timeit('my_prime(600)', number=1000, globals=globals()))  # 9.178990499999998
# print(timeit.timeit('my_prime(700)', number=1000, globals=globals()))  # 12.528298300000017
# print(timeit.timeit('my_prime(800)', number=1000, globals=globals()))  # 16.50986690000002
# print(timeit.timeit('my_prime(900)', number=1000, globals=globals()))  # 20.790303600000016
# print(timeit.timeit('my_prime(1000)', number=1000, globals=globals()))  # 25.739074699999946
# print(timeit.timeit('my_prime(1100)', number=1000, globals=globals()))  # 31.17761509999991
# print(timeit.timeit('my_prime(1200)', number=1000, globals=globals()))  # 37.11852680000004
# print(timeit.timeit('my_prime(1300)', number=1000, globals=globals()))  # 43.531877099999974
# print(timeit.timeit('my_prime(1400)', number=1000, globals=globals()))  # 50.57701470000006
# print(timeit.timeit('my_prime(1500)', number=1000, globals=globals()))  # 58.145990199999915

# print(timeit.timeit('my_prime(1000)', number=1000, globals=globals()))  # 25.75989840000011
# print(timeit.timeit('my_prime(2000)', number=1000, globals=globals()))  # 109.06695330000002
# print(timeit.timeit('my_prime(3000)', number=1000, globals=globals()))  # 238.32370579999997
# print(timeit.timeit('my_prime(4000)', number=1000, globals=globals()))  # 482.72883990000037
# print(timeit.timeit('my_prime(5000)', number=1000, globals=globals()))  # 873.7611865999997
# print(timeit.timeit('my_prime(6000)', number=1000, globals=globals()))  # 1379.616212


cProfile.run('my_prime(100)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 Task_2.py:33(my_prime)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('my_prime(1000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.025    0.025 <string>:1(<module>)
#         1    0.025    0.025    0.025    0.025 Task_2.py:33(my_prime)
#         1    0.000    0.000    0.025    0.025 {built-in method builtins.exec}
#       999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('my_prime(5000)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.893    0.893 <string>:1(<module>)
#         1    0.893    0.893    0.893    0.893 Task_2.py:33(my_prime)
#         1    0.000    0.000    0.893    0.893 {built-in method builtins.exec}
#      4999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#  google doc с графиком:
# https://docs.google.com/spreadsheets/d/1NLJ3yGUX7hElTZ78RU4zIlkMAOMfMaQHyvM4WINrkKA/edit?usp=sharing
#  Замеры производились на разных объемах данных. от 100 до 1500  с шагом 100 и от 1000 до 5000 с шагом 1000.
#  На графике по ссылке выше видно, что в целом обе функции работают примерно одинаково по времени.
#  Разница не значительная. Она видна только в моменте, когда функция с решетом получает объем данных свыше 1000,
# в этот момет время выростает практически в 2 раза, по сравнению с объемом до 1000,
# но затем обе функции трятят примерно одно и тоже время на обработку.
# Вариант без решета вызывает меньше функций примерно в 4 раза.
# Я бы назвал линейной функцию my_prime(), а функцию eratosthenes_sieve() я затрудняюсь назвать)
# до определенного момента она похожа на линейную, но затем после определенно количества данных
# она приобритает квадратичность, а затем опять продолжает работу как линейная...)
