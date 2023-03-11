# Task 1
users_login = input("Введите логин: ")
users_password = input("Введите пароль: ")

login = "user"
password = "qwerty"
if login == users_login and password == users_password:
    print("Authentication completed")
else:
    print("Invalid login or password")


# Task 2
amount = float(input("Insert amount in KZT: "))
currency = int(input("Choose currency:\n[1] USD\n[2] EUR\n[3] RUB\n"))

usd = 420
eur = 510
rub = 5.8

if currency == 1:
    converted_amount = amount / usd
    print("{:.2f} USD".format(converted_amount))
elif currency == 2:
    converted_amount = amount / eur
    print("{:.2f} EUR".format(converted_amount))
elif currency == 3:
    converted_amount = amount / rub
    print("{:.2f} RUB".format(converted_amount))
else:
    print("Invalid currency selected.")
