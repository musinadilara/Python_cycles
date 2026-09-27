
x_beg = -10
x_end = 8
step = float(input('Введите шаг(целое неотрицательное число): '))
print('   x  |  y')

while x_beg <= x_end:
    if x_beg <= -8:
        y = -3
    elif x_beg <= -3:
        y = -3 + (8 + x_beg) * 0.6
    elif x_beg <= 3:
        y = (9 - x_beg ** 2) ** 0.5
    elif x_beg <= 5:
        y = x_beg - 3
    else: y = 3
    print((4 - len(str(round(x_beg))))*' ', round(x_beg) , '|', y)

    x_beg += step