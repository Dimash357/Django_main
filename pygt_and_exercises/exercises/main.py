# Task 1
user_string = input("Enter your string: ")
words = user_string.split()
reversed_string = ' '.join(reversed(words))
print(reversed_string)

# Task 2
user_string = input("Enter your string: ")
words = user_string.split()
word_count = len(words)
print(word_count)

# Task 3
user_string = input("Enter your string: ")
new_string = user_string.replace('2020', '2021')
print(new_string)

# Task 4
numbers = []
print("Enter your numbers:")
while True:
    num = int(input())
    numbers.append(num)
    if sum(numbers) == 0:
        break
squares_sum = sum([x*x for x in numbers])
print(f"\n{squares_sum}")