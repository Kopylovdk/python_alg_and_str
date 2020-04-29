# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
import hashlib


def subs_count(value):
    file = open('subs.txt', 'w', encoding='utf-8')
    file.close()
    value_len = len(value)
    spam = True
    x = 1
    while x < value_len:
        eggs = set()
        for i in range(value_len - x):
            if value != value[i:i + x + 1]:
                eggs.add(hashlib.sha1(value[i:i + x + 1].encode('utf-8')).hexdigest())
        if spam:
            for i in value:
                eggs.add(hashlib.sha1(i.encode('utf-8')).hexdigest())
            spam = False
        with open('subs.txt', 'a', encoding='utf-8') as file:
            for i in eggs:
                file.writelines(i + '\n')
            file.close()
        x += 1
    print(f'Файл subs.txt с Хэшами записан. Начинаем подсчет строк.')
    with open('subs.txt', 'r', encoding='utf-8') as file:
        hash_subs = sum(1 for i in file)
        file.close()
    return f'Была передана строка длиной: {len(value)}.\nВсего {hash_subs} подстрок.'


a = input('Введите строку для подсчета подстрок: ')
print(subs_count(a))
