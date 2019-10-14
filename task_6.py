import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_number = array[0]
min_number = array[0]
imax = 0
imin = 0

print('Сгенерированный массив случайных натуральных чисел:', array)

for i in range(1, SIZE):
    if array[i] >= max_number:
        max_number = array[i]
        imax = i
    elif array[i] <= min_number:
        min_number = array[i]
        imin = i

if imax < imin: # Тут практически всё взял из задачи с заменой максимумов/минимумов, кроме этого блока
    help_var = array[imax] # Замена местами макс. и мин. как в 3 задаче
    array[imax] = array[imin]
    array[imin] = help_var

    help_var_2 = imax # Замена индексов по аналогии
    imax = imin
    imin = help_var_2

summ = 0

for i in range(imin + 1, imax):
    summ = array[i] + summ

print(f'\nМаксимальный элемент массива: {array[imax]} (Индекс в массиве: {imax})')
print(f'Минимальный элемент массива: {array[imin]} (Индекс в массиве: {imin})')
print('\nСумма элементов массива между минимальным и максимальным элементами (не включая их): ', summ)