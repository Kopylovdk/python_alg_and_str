# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
columns = 3
lines = 5
matrix = []
for i in range(lines):
    sum_line = 0
    line = []
    for j in range(columns):
        value = int(input(f'Введите зачение {j+1} строки {i+1}: '))
        sum_line += value
        line.append(value)
    line.append(sum_line)
    matrix.append(line)

for i in matrix:
    for j in i:
        print(f'{j:>5}', end='')
    print()
