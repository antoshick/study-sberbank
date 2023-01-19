"""
Дана строка: Abracadabra
Требуется:
"""
st = "Abracadabra"

# 1. Вывести третий символ этой строки.
print(st[2])

# 2. Вывести предпоследний символ этой строки.
print(st[-1])

# 3. Вывести первые пять символов этой строки.
print(st[:5])

# 4. Вывести строку, кроме последних двух символов.
a = int(len(st)-2)
print(st[:a])

# 5. Вывести все символы с четными индексами (считайте, что 0 - четный индекс).
st2 = ""
ln = -1
for i in st:
    ln += 1
    if ln % 2 == 0:
        st2 = st2 + i
print(st2)

# 6. Вывести все символы с нечетными индексами.
st2 = ""
ln = 0
for i in st:
    ln += 1
    if ln % 2 == 0:
        st2 = st2 + i
print(st2)

# 7. Вывести все символы в обратном порядке.
print(st[::-1])

# 8. Вывести все символы строки через один в обратном порядке, начиная с последнего.
st2 = ""
ln = -1
for i in st[::-1]:
    ln += 1
    if ln % 2 == 0:
        st2 = st2 + i
print(st2)

# 9. Вывести длину данной строки.
print(len(st))