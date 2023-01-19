# О Б М Е Н Н Ы Й   К У Р С
"""
В 1-ом тугрике 17-ть чогриков, а в одном чогрике 13-ть песо.
Определите, на какое число тугриков и чогриков можно обменять n песо, если провести
все возможные операции. На вход программа получает одно натуральное
число --- количество песо, а в количестве результата выводит три натуральных числа
разделённые пробелом:
число Тугриков, число Чогриков, число оставшихся Песо
"""
# Входные данные:
peso = 40
# Выходные данные: 0 3 1
pes = abs(3 * 13 - peso)
cho = int(peso / 13)
tug = int(cho / 17)
print(tug, cho, pes)

# Входные данные:
peso = 1300
# Выходные данные: 5 15 0
tug = int(peso / 13 / 17)
cho = int((peso - (tug * 13 * 17)) / 13)
pes = 0
print(tug, cho, pes)
# Входные данные:
peso = 7623
# Выходные данные: 34 8 5
tug = int(peso / 13 / 17)
cho = int((peso - (tug * 13 * 17)) / 13)
pes = peso - (tug * 13 * 17 + cho * 13)
print(tug, cho, pes)
# Входные данные:
peso = 2132
# Выходные данные: 9 11 0
tug = int(peso / 13 / 17)
cho = int((peso - (tug * 13 * 17)) / 13)
pes = peso - (tug * 13 * 17 + cho * 13)
print(tug, cho, pes)
# Входные данные:
peso = 221
# Выходные данные: 1 0 0
tug = int(peso / 13 / 17)
cho = int((peso - (tug * 13 * 17)) / 13)
pes = int(peso - (tug * 13 * 17 + cho * 13))
print(tug, cho, pes)