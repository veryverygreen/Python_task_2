import re

input_list = int(input())

if input_list < 0:
    print ('Введено отрицательное число')  #проверка на положительное число
else:
    try:
        int(input_list)  # проверка на целое число
        square_numbers = int(re.sub('\d', lambda m: str(int(m.group(0)) ** 2), str(input_list)))
        print (f'Квадрат каждой цифры из числа = {square_numbers}')
    except:
        print ('Введено не целое число')