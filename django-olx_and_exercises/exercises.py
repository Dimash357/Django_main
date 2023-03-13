# Task 1
ticket = input("Введите 6-значное число: ").strip()
left_sum = sum(int(i) for i in ticket[:3])
right_sum = sum(int(i) for i in ticket[3:])

if left_sum == right_sum:
    print("Счастливый")
else:
    print("Обычный")


# Task 2
a = int(input("Введите кол-во людей в команде биологов: "))
b = int(input("Введите кол-во людей в команде информатиков: "))
NOK = max(a, b)

while NOK % a != 0 or NOK % b != 0:
    NOK += 1

print(NOK)
