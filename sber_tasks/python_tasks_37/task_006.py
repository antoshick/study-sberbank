# Б У К В Е Н Н О Е   Р А С С Т О Я Н И Е
"""
Определим буквенное расстояние как сумму модулей разностей количества вхождения, букв
в этих стоках.
Например, буквенное расстояние между строками "abcde" и "aaaee" равно 6:
буквы a, b, c, d, e входят в первую строку по одному разу, во вторую строку
входят три буквы a и две буквы e: [3-1]+[1-0]+[1-0]+[1-0]+[2-1] = 6
Найдите буквенное расстояние между двумя строками.
На вход программа получает две строки, на выходе
печатает натуральное число - буквенное расстояние между строками.
"""
# Входные данные:
s1, s2 = "wgrlpdxcfdhtte", "tvsajfjbygwzri"
# Выходные данные: 18
s1 = sorted(list(s1))
s2 = sorted(list(s2))
s3 = sorted(s1 + s2)
# print(s3)
s4 = sorted(set(s3))
# print(s4)
sm = 0
for i in s4:
    # print(f"{i} = {s1.count(i)}, {i} = {s2.count(i)}, {abs(s1.count(i)-s2.count(i))}")
    sm = sm + abs(s1.count(i)-s2.count(i))
print(sm)

# Входные данные:
s1 = "eetttkqczlan"
s2 = "aknmixwowgol"
# Выходные данные: 16
s1 = sorted(list(s1))
s2 = sorted(list(s2))
s3 = sorted(s1 + s2)
# print(s3)
s4 = sorted(set(s3))
# print(s4)
sm = 0
for i in s4:
    # print(f"{i} = {s1.count(i)}, {i} = {s2.count(i)}, {abs(s1.count(i)-s2.count(i))}")
    sm = sm + abs(s1.count(i)-s2.count(i))
print(sm)
# Входные данные:
s1 = "geppojoi"
s2 = "qsehksew"
# Выходные данные: 14
s1 = sorted(list(s1))
s2 = sorted(list(s2))
s3 = sorted(s1 + s2)
# print(s3)
s4 = sorted(set(s3))
# print(s4)
sm = 0
for i in s4:
    # print(f"{i} = {s1.count(i)}, {i} = {s2.count(i)}, {abs(s1.count(i)-s2.count(i))}")
    sm = sm + abs(s1.count(i)-s2.count(i))
print(sm)
# Входные данные:
s1 = "abcde"
s2 = "edcba"
# Выходные данные: 0
s1 = sorted(list(s1))
s2 = sorted(list(s2))
s3 = sorted(s1 + s2)
# print(s3)
s4 = sorted(set(s3))
# print(s4)
sm = 0
for i in s4:
    # print(f"{i} = {s1.count(i)}, {i} = {s2.count(i)}, {abs(s1.count(i)-s2.count(i))}")
    sm = sm + abs(s1.count(i)-s2.count(i))
print(sm)
# Входные данные:
s1 = "wrhsj"
s2 = "nbwra"
s1 = sorted(list(s1))
s2 = sorted(list(s2))
s3 = sorted(s1 + s2)
# print(s3)
s4 = sorted(set(s3))
# print(s4)
sm = 0
for i in s4:
    # print(f"{i} = {s1.count(i)}, {i} = {s2.count(i)}, {abs(s1.count(i)-s2.count(i))}")
    sm = sm + abs(s1.count(i)-s2.count(i))
print(sm)
# Выходные данные: 6
