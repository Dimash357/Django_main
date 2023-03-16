# Task 1
n = int(input("Number of cards: "))
sum_all = (n * (n + 1)) // 2
sum_cards = sum(int(input("Cards: ")) for i in range(n-1))
missing_card = sum_all - sum_cards
print(missing_card)


# Task 2
n = int(input("Number: "))
for i in range(1, int(n**0.5) + 1):
    result = i ** 2
    if result <= n:
        print(result)
