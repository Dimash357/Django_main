# Task 1
# Рекурсия
def is_palindrome_recursive(string1):
    string1 = string1.lower().replace(" ", "").replace(",", "").replace("'", "")
    if len(string1) < 2:
        return True
    if string1[0] != string1[-1]:
        return False
    return is_palindrome_recursive(string1[1:-1])


string1 = "Казак"
print(is_palindrome_recursive(string1))


# Реверс строки
def is_palindrome_reverse(string2):
    string2 = string2.lower().replace(" ", "").replace(",", "").replace("'", "")
    reversed_string2 = string2[::-1]
    return string2 == reversed_string2


string2 = "А роза упала на лапу Азора"
print(is_palindrome_reverse(string2))


# Метод двух указателей
def is_palindrome_pointers(string3):
    string3 = string3.lower().replace(" ", "").replace(",", "").replace("'", "")
    left = 0
    right = len(string3) - 1
    while left < right:
        if string3[left] != string3[right]:
            return False
        left += 1
        right -= 1
    return True


string3 = "Madam, I'm Adam"
print(is_palindrome_pointers(string3))


# Task 2
"""
Для удобства:(для себя)
1) Отсортировать список целых чисел.
2) Создать переменные start и end, которые будут обозначать начало и конец текущего диапазона.
3) Создать пустую строку result.
4) Проходя по элементам списка целых чисел, проверять, является ли текущий элемент следующим по числовому ряду от предыдущего элемента.
       Если является, то обновлять переменную end, чтобы она указывала на текущий элемент.
            Если не является, то:
            Если start и end равны, то добавить start в строку result.
            Если start и end отличаются, то добавить диапазон start-end в строку result.
            Обновить переменную start, чтобы она указывала на текущий элемент.
            Обновить переменную end, чтобы она указывала на текущий элемент.
5) Если после прохода по всем элементам start и end указывают на один и тот же элемент, то добавить его в строку result. Если start и end отличаются, то добавить диапазон start-end в строку result.
6) Вернуть строку result.
"""


def second_algoritm(list1):
    list1.sort()
    start = end = list1[0]
    result = ""
    for i in range(1, len(list1)):
        if list1[i] == end + 1:
            end = list1[i]
        else:
            if start == end:
                result += str(start) + ","
            else:
                result += str(start) + "-" + str(end) + ","
            start = end = list1[i]
    if start == end:
        result += str(start)
    else:
        result += str(start) + "-" + str(end)
    return result


print(second_algoritm([1, 4, 5, 2, 3, 9, 8, 11, 0]))
print(second_algoritm([1, 4, 3, 2]))
print(second_algoritm([1, 4]))
