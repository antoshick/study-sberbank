"""
Задан массив из n чисел. Напишите программу, которая выводит количество
чисел равных нулю.
Подставьте "Входные данные" в свою программу и сравните результат с выходными данными.
# 1) Входные данные: 0, 1, 2, 3, 4. Выходные данные: 1
# 2) Входные данные: 1, 0, 1, 0, 1, 0, 1, 0, 1, 0. Выходные данные: 5
# 3) Входные данные: 8, 4, 0, 3, 9, 2, 3, 0. Выходные данные: 2
# 4) Входные данные: 700, 8, 89, 20, 13. Выходные данные: 0
"""
u_ar1 = [0, 1, 2, 3, 4]
u_ar2 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
u_ar3 = [8, 4, 0, 3, 9, 2, 3, 0]
u_ar4 = [700, 8, 89, 20, 13]

u_ar = [u_ar1, u_ar2, u_ar3, u_ar4]
u_l_s_a = []
tax1, tax2, tax3, tax4 = 0, 0, 0, 0

for i in u_ar[0]:
    if i == 0:
        tax1 += 1
u_l_s_a.append(tax1)
# print(tax1)
for i in u_ar[1]:
    if i == 0:
        tax2 += 1
u_l_s_a.append(tax2)
# print(tax2)
for i in u_ar[2]:
    if i ==0:
        tax3 += 1
u_l_s_a.append(tax3)
# print(tax3)
for i in u_ar[3]:
    if i == 0:
        tax4 += 1
u_l_s_a.append(tax4)
# print(tax4)
print(u_l_s_a)