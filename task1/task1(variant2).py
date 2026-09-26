
x_beg = -10
x_end = 8
step = int(input('Введите шаг(неотрицательное число): '))
print(' x  |  y')

while x_beg <= x_end:
    if x_beg >= -8: y = -3
    elif  x_beg <= -3:
    elif x_beg >= 0:
    print(x + ' | ' + y)
    x_beg += step