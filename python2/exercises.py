# Task 1
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(1, 11):
    print(f"fibonacci number {i} = {fibonacci(i)}")


# Task 2
def is_power_of_two(n):
    if n <= 0:
        return False
    else:
        return (n & (n-1)) == 0


n = 8
print(is_power_of_two(n))  # True

n = 7
print(is_power_of_two(n))  # False


# Task 3
import math


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Факториал")
print("7. Число Фибоначчи")
print("8. sin")
print("9. cos")
print("10. tan")

choice = input("Введите номер операции (1-10): ")

if choice in ('1', '2', '3', '4', '5'):
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))

    if choice == '1':
        print(x, "+", y, "=", x + y)

    elif choice == '2':
        print(x, "-", y, "=", x - y)

    elif choice == '3':
        print(x, "*", y, "=", x * y)

    elif choice == '4':
        if y == 0:
            print("Деление на ноль невозможно")
        else:
            print(x, "/", y, "=", x / y)

    elif choice == '5':
        print(x, "**", y, "=", x ** y)

elif choice == '6':
    n = int(input("Введите число: "))
    print(factorial(n))

elif choice == '7':
    n = int(input("Введите число: "))
    print(fibonacci(n))

elif choice in ('8', '9', '10'):
    x = float(input("Введите угол в градусах: "))
    radians = math.radians(x)

    if choice == '8':
        print("sin({}) = {}".format(x, math.sin(radians)))

    elif choice == '9':
        print("cos({}) = {}".format(x, math.cos(radians)))

    elif choice == '10':
        print("tan({}) = {}".format(x, math.tan(radians)))

else:
    print("Некорректный ввод")


# Task 4
def print_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for col in row:
            print(col, "|", end=" ")
        print("\n-------------")


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None


def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    winner = None
    while not winner:
        print_board(board)
        move = input(f"Куда поставим {player}? ")
        row, col = (int(move) - 1) // 3, (int(move) - 1) % 3
        if board[row][col] != " ":
            print("Эта ячейка уже занята, попробуйте еще раз.")
            continue
        board[row][col] = player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{winner} выиграл!")
        elif " " not in [col for row in board for col in row]:
            print_board(board)
            print("Ничья!")
            break
        else:
            player = "O" if player == "X" else "X"


play()
