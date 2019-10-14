# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Сгенерированный массив чисел: ', array)

max_negative = array[0]
i = 0
# в данном блоке перебираем весь массив до того как попадется первое отр. число
# как только мы его находим, то назначаем его максимальным отрицательным

while i < SIZE:
    i += 1
    if array[i] < 0:
        max_negative = array[i]
        break # Здесь мы нашли первый отрицательный элемент массива, занесли его в макс. и выходим из цикла
    elif array[i] > 0 and i == SIZE - 1:
        print('В данном массиве нет отрицательных чисел')
        break # Здесь мы выходим из цикла, как только выполняется условие что все элементы положительные

if max_negative < 0:
            # Макс. отриц. число - отр. число с наименьшим по значению модулем. Сравниваем модули чисел в цикле:
    for i in range(0, SIZE):
        if array[i] < 0 and abs(array[i]) < abs(max_negative):
            max_negative = array[i]

    print('\nМаксимальное отрицательное число массива: ', max_negative)
    print('Индекс максимального отрицательного числа в массиве: ', array.index(max_negative))