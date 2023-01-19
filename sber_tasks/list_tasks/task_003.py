"""
Задан список с числами. Напишите программу, которая меняет местами
наибольший и наименьший элемент
Подставьте "Входные данные" в свою программу и сравните результат с выходными данными.
"""
# 1) Входные данные: 3, 4, 5, 2, 1. Выходные данные: 3, 4, 1, 2, 5
lst = [3, 4, 5, 2, 1]
mx = max(lst)
mn = min(lst)
imn = lst.index(min(lst))
imx = lst.index(max(lst))
lst2 = lst.copy()
lst2.remove(mn)
lst2.remove(mx)
lst2.insert(imn, mx)
lst2.insert(imx, mn)
# in_mx = lst.index(max(lst))
# in_mn = lst.index(min(lst))
print(f"Входные данные {lst}\nВыходные данные {lst2}")

# 2) Входные данные: -3000, 3000. Выходные данные: 3000, -3000
lst = [-3000,3000]
mx = max(lst)
mn = min(lst)
imn = lst.index(min(lst))
imx = lst.index(max(lst))
lst2 = lst.copy()
lst2.remove(mn)
lst2.remove(mx)
lst2.insert(imn, mx)
lst2.insert(imx, mn)
# in_mx = lst.index(max(lst))
# in_mn = lst.index(min(lst))
print(f"Входные данные {lst}\nВыходные данные {lst2}")

# 3) Входные данные: 1, 2, 3, 4, 5, 6, 7. Выходные данные: 7, 2, 3, 4, 5, 6, 1
lst = [1, 2, 3, 4, 5, 6, 7]
mx = max(lst)
mn = min(lst)
imn = lst.index(min(lst))
imx = lst.index(max(lst))
lst2 = lst.copy()
lst2.remove(mn)
lst2.remove(mx)
lst2.insert(imn, mx)
lst2.insert(imx, mn)
# in_mx = lst.index(max(lst))
# in_mn = lst.index(min(lst))
print(f"Входные данные {lst} Выходные данные {lst2}")

# 4) Входные данные: -5, 5, 10. Выходные данные: 10, 5, -5
lst = [-5, 5, 10]
mx = max(lst)
mn = min(lst)
imn = lst.index(min(lst))
imx = lst.index(max(lst))
lst2 = lst.copy()
lst2.remove(mn)
lst2.remove(mx)
lst2.insert(imn, mx)
lst2.insert(imx, mn)
# in_mx = lst.index(max(lst))
# in_mn = lst.index(min(lst))
print(f"Входные данные {lst} Выходные данные {lst2}")