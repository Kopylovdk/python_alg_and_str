# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
for i in range(2, 10):
    print(f'Кратно {i} - {99 // i}')
