#\*************************/#
#\*******Te3K@_PaynE*******/#
#\**79811131773@yandex.ru**/#
#\*************************/#

'''
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai.
(В нашем случае массив генерируется случайным целыми числами от 0 до 999)
Последняя строка содержит число X

*Пример:*
5
1 2 3 4 5
6
-> 5
'''
import random

# Функция вывода автора программы
def author():
    print('****************************')
    print('Программа создана:')
    print('Илья "Te3K@_PaynE" Новичихин')
    print('79811131773@yandex.ru')
    print('****************************')

# Проверка на введение положительного числа.
def correct_number():
    _number = int(input("Введите количество элементов в массиве: "))
    while (_number < 0):
        _number = int(input("Введено неверное число! Введите заново: "))
    return _number

# Создание массива случайных чисел
def generate_random_list(_min, _max, _num):
    _list = []
    for i in range(int(_num)):
        _list.append(random.randint(_min, _max))
    return _list

def find_element(_list, _num):
    _index = 0
    _diff = abs(_num - _list[_index])
    for _i in range(len(_list)):
        if abs(_num - _list[_i]) < _diff:
            _diff = abs(_num - _list[_i])
            _index = _i
    return _index

print("Программа выводит на экран наиболее близкое к введённому числу элемент массива случайных чисел,\n" + 
      "в котором количество элементов задаётся пользователем.")
_num = correct_number()
_list_rand_num = generate_random_list(0, 99, _num)
print(_list_rand_num)
_x = int(input("Какое число будем искать 0 до 99? x = "))
_element = find_element(_list_rand_num, _x)
print(f"Наиболее близкий элемент к числу {_x} - это {_list_rand_num[_element]}")

author()