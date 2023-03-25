# Task 1
grades = list(map(int, input("Оценки: ").split()))

fives = grades.count(5)
fours = grades.count(4)
threes = grades.count(3)
twos = grades.count(2)

average = sum(grades) / len(grades)

print(f"{fives} {fours} {threes} {twos}")
print(average)


# Task 2
grades = list(map(int, input("Оценки: ").split()))

for i in range(len(grades)):
    if grades[i] == 2:
        grades[i] = 3

print(*grades)


# Task 3
n = int(input("Длина списка: "))
lst = list(map(int, input("Число: ").split()))

evens = [num for num in lst if num % 2 == 0]
odds = [num for num in lst if num % 2 != 0]

if len(odds) > len(evens):
    print("Нет")
else:
    print("Да")

print(*odds)
print(*evens)


# Task 4
def create_matrix():
    matrix = []
    for i in range(3):
        row = list(map(int, input("Число: ").split()))
        matrix.append(row)
    return matrix

def sum_diagonal(matrix):
    diagonal_sum = 0
    for i in range(3):
        diagonal_sum += matrix[i][i]
    return diagonal_sum

matrix = create_matrix()
diagonal_sum = sum_diagonal(matrix)
print(diagonal_sum)


# Task 5
def get_user_info():
    name = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    email = input("Введите вашу электронную почту: ")
    phone = input("Введите ваш номер телефона: ")
    city = input("Введите ваш город проживания: ")

    return name, age, email, phone, city


def print_cv(name, age, email, phone, city):
    print("=" * 30)
    print("CV")
    print("=" * 30)
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    print(f"Электронная почта: {email}")
    print(f"Номер телефона: {phone}")
    print(f"Город проживания: {city}")
    print("=" * 30)


name, age, email, phone, city = get_user_info()
print_cv(name, age, email, phone, city)