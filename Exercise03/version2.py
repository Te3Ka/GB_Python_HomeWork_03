#\*************************/#
#\*******Te3K@_PaynE*******/#
#\**79811131773@yandex.ru**/#
#\*************************/#

'''
 В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
 В случае с английским алфавитом очки распределяются так:
 A, E, I, O, U, L, N, S, T, R – 1 очко;
 D, G – 2 очка;
 B, C, M, P – 3 очка;
 F, H, V, W, Y – 4 очка;
 K – 5 очков;
 J, X – 8 очков;
 Q, Z – 10 очков.

 А русские буквы оцениваются так:
 А, В, Е, И, Н, О, Р, С, Т – 1 очко;
 Д, К, Л, М, П, У – 2 очка;
 Б, Г, Ё, Ь, Я – 3 очка;
 Й, Ы – 4 очка;
 Ж, З, Х, Ц, Ч – 5 очков;
 Ш, Э, Ю – 8 очков;
 Ф, Щ, Ъ – 10 очков.
 
 Напишите программу, которая вычисляет стоимость введенного пользователем слова.
 Будем считать, что на вход подается только одно слово,
 которое содержит либо только английские, либо только русские буквы.

*Пример:*
ноутбук
--> 12
'''
import random

# Функция вывода автора программы
def author():
    print('****************************')
    print('Программа создана:')
    print('Илья "Te3K@_PaynE" Новичихин')
    print('79811131773@yandex.ru')
    print('****************************')

alphabet_english = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
                    'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
                    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
                    'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
                    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4,
                    'z': 10}

alphabet_russian = {'а': 1, 'б': 3, 'в': 1, 'г': 3, 'д': 2,
                    'е': 1, 'ё': 3, 'ж': 5, 'з': 5, 'и': 1,
                    'й': 4, 'к': 2, 'л': 2, 'м': 2, 'н': 1,
                    'о': 1, 'п': 2, 'р': 1, 'с': 1, 'т': 1,
                    'у': 2, 'ф': 10, 'х': 5, 'ц': 5, 'ч': 5,
                    'ш': 8, 'щ': 10, 'ъ': 10, 'ы': 4, 'ь': 3,
                    'э': 8, 'ю': 8, 'я': 3}

print("Программа считает количество очков введённого слова для игры Scrabble по классическим правилам игры")
_word = str(input("Введите русское или английское слово (только одно!) = "))
_points = 0
_word = _word.lower()
print(_word)
for _letter in _word:
    if _letter in alphabet_english:
        _points += alphabet_english[_letter]
    elif _letter in alphabet_russian:
        _points += alphabet_russian[_letter]
    else:
        print("Неизвестный алфавит")
print(_points)

author()