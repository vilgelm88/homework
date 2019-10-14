import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_number = array[0] #Изначально задаем максимум первым элементом массива
min_number = array[0] #Изначально задаем минимум первым элементом массива
imax = 0 #По умолчанию ставим индекс максимального элемента массива первым
imin = 0

print('Сгенерированный массив случайных натуральных чисел:', array)

#Перебираем массив (со 2-го элемента (1-й в python) до 10 го включительно (9-й в python)):

for i in range(1, 10):
    if array[i] >= max_number:
        max_number = array[i]
        imax = i
    elif array[i] <= min_number:
        min_number = array[i]
        imin = i

print(f'\nМаксимум массива {max_number}, Индекс в массиве: {imax}')
print(f'Максимум массива {min_number}, Индекс в массиве: {imin}')

help_var = array[imax]
array[imax] = array[imin]
array[imin] = help_var

print('\nПолученный массив с замененными экстремумами:', array)