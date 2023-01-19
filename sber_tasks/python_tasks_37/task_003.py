# П Р О Ш Л Ы Е   В С Т Р Е Ч И
"""
Во входной строке записана последовательность чисел, отделённых пробелами.
Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось
в последовательности, и NO если не встречалось.
"""
# Входные данные:
inst = "1 2 3 2 3 4"
# Выходные данные: NO NO NO YES YES NO
"""inl = inst.split(" ")
print(inl)
c = 0
for i in inl:
    if c == 0:
        print("NO")
    c = c + 1
    inl2 = inl[0:c]
    print(inl2)
"""
# Входные данные:
inst = "1 2 3 4 5 6"
# Выходные данные:NO NO NO NO NO NO
inl = inst.split(" ")
c = 0
for i in inl:

    inl2 = inl[c:-1]
    # print(inl2)
    if len(inl2) == 1:
        print("NO")
    if len(inl2) >= 2:
        if inl2.count(inl2[-1]) > 1:
            print("YES")
        else:
            print("NO")
    c = c + 1

# Входные данные:
inst = "1 -1 1 -1 1 -1"
# Выходные данные: NO NO YES YES YES YES
inl = inst.split(" ")
c = 0
for i in inl:

    inl2 = inl[c:-1]
    # print(inl2)
    if len(inl2) == 1:
        print("NO")
    if len(inl2) >= 2:
        if inl2.count(inl2[-1]) > 0:
            print("YES")
        else:
            print("NO")
    c = c + 1
# Входные данные:
inst = "0 0 0 0 0 0"
# Выходные данные: NO YES YES YES YES YES
inl = inst.split(" ")
c = 0
for i in inl:

    inl2 = inl[:c]
    # print(inl2)
    if len(inl2) == 1:
        print("NO")
    if len(inl2) >= 2:
        if inl2.count(inl2[-1]) > 0:
            print("YES")
        else:
            print("NO")
    c = c + 1