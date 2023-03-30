# Task 1
def calculate_min_cost(items):
    items.sort(reverse=True)
    total_cost = sum(items)
    discount = sum(items[:2])
    return total_cost - discount


items = [1, 5, 4, 3, 5, 7]
min_cost = calculate_min_cost(items)
print(min_cost)


# Task 2
def closest_numbers(numbers):
    numbers = sorted(numbers)

    min_diff = float('inf')
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        if diff < min_diff:
            min_diff = diff

    pairs = []
    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] == min_diff:
            pairs.append((numbers[i], numbers[i+1]))

    for pair in pairs:
        print(pair[0], pair[1])


numbers = [9, 4, 1, 6]
closest_numbers(numbers)


# Task 3
def align_strings(strings):
    max_len = max([len(s) for s in strings])

    for s in strings:
        print('*'*(max_len - len(s)) + s)


M = int(input("Введите количесво строк: "))
strings = []
for i in range(M):
    s = input()
    strings.append(s)

align_strings(strings)


# Task 4
def add_element_to_balance(arr):
    pos_sum = sum(filter(lambda x: x > 0, arr))
    neg_sum = abs(sum(filter(lambda x: x < 0, arr)))

    new_elem = neg_sum - pos_sum

    arr.append(new_elem)

    return arr


arr = [-3, -2, 1, 2, 3, 4]
result = add_element_to_balance(arr)
print(result)