# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

number = int(input('Введите число: '))
rev_number = 0

while number > 0:
    rev_number = rev_number * 10 + number % 10
    number = number // 10
print('Полученное обратное число: ', rev_number)

# если на конце 0 то не работает. если бы можно было использовать массивы