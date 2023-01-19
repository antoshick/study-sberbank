"""
Задан список с числами. Напишите программу, которая выводит все элементы
списка, которые больше предыдущего, в виде отдельного списка.
Подставьте "Входные данные" в свою программу и сравните результат с выходными данными.
"""
# 1) Входные данные: 1, 5, 2, 4, 3. Выходные данные: 5, 4
lst = [1, 5, 2, 4, 3]
lst2 = []
lst.append(lst[-1])
for i in lst:
    i = lst[0]
    if i < lst[1]:
        lst2.append(lst[1])
    lst.remove(lst[0])
print(lst2)

# 2) Входные данные: 1, 2, 3, 4, 5. Выходные данные: 2, 3, 4, 5
lst = [1, 2, 3, 4, 5]
lst2 = []
lst.append(lst[-1])
for i in lst:
    i = lst[0]
    if i < lst[1]:
        lst2.append(lst[1])
    lst.remove(lst[0])
print(lst2)

# 3) Входные данные: 5, 4, 3, 2, 1. Выходные данные:
lst = [5, 4, 3, 2, 1]
lst2 = []
lst.append(lst[-1])
for i in lst:
    i = lst[0]
    if i < lst[1]:
        lst2.append(lst[1])
    lst.remove(lst[0])
print(lst2)

# 4) Входные данные: 1, 5, 1, 5, 1. Выходные данные: 5, 5
lst = [1, 5, 1, 5, 1]
lst2 = []
lst.append(lst[-1])
for i in lst:
    i = lst[0]
    if i < lst[1]:
        lst2.append(lst[1])
    lst.remove(lst[0])
print(lst2)


