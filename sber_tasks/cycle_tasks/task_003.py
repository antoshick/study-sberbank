"""
По данному натуральному числу n <= 9 выведите лесенку из n ступенек,
i-я ступенька состоит из чисел от 1 до i без пробелов.
1) Входные данные: 5. Выходные данные:
1
12
123
1234
12345
"""
u_i = int(input('Введите данные: '))
u_s = ""
for i in range(1, u_i+1):
    u_s = u_s + str(i)
    print(u_s)


