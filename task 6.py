

import random

number = random.randint(0, 100)

counter = 1
print('Пожалуйста попробуйте угадать число с 10 попыток')

while counter <= 10:
    user_number = int(input(f'Введите число (попытка № {counter}): '))
    if user_number > number:
        print('Введенное число больше загаданного')
    elif user_number < number:
        print('Введенное число меньше загаданного')
    elif user_number == number:
        print(f'Поздравляю! Вы угадали число с {counter} попытки')
        break
    counter += 1
else:
    print('У вас закончились попытки. Загаданное число: ', number)