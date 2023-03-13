# Task 1
ticket = input("Введите 6-значное число: ").strip()
left_sum = sum(int(i) for i in ticket[:3])
right_sum = sum(int(i) for i in ticket[3:])

if left_sum == right_sum:
    print("Счастливый")
else:
    print("Обычный")


# Task 2
import math
a = int(input("Введите кол-во первой команды: "))
b = int(input("Введите кол-во второй команды: "))

NOD = math.gcd(a, b)
NOK = a * b // NOD

print(NOK)




