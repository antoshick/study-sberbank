"""
Бонусное задание вариант 1.
        1
       12
      123
     1234
    12345
   123456
  1234567
 12345678
123456789
         987654321
         87654321
         7654321
         654321
         54321
         4321
         321
         21
         1
"""
n = int(input('Введите число ступеней меньше 10: '))
if n > 9:
    print('Ошибка, количество ступеней должно быть меньше 10')
else:
    for i in range(1,n+1):
        step=' '*(n-i)
        for j in range(1,i+1):
            step+= str(j)
        for j in range(i-1,0,-1):
            step+= str(j)
        print(step)
    for i in range(n-1,0,-1):
        step=' '*(n-i)
        for j in range(1,i+1):
            step += str(j)
        for j in range(i-1,0,-1):
            step += str(j)
        print(step)
