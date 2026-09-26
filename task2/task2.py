
polindroms = []

for number in range(10, 100):
    sq_number = number ** 2
    if str(sq_number) == str(sq_number)[::-1]:
        polindroms.append(number)

print(*polindroms)
