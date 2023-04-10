# Task 1
# С этим заданием помог немного chatGPT
candidates = ['Аскаров', 'Бекмуханов', 'Ернур', 'Пешая', 'Карим', 'Шаримазданов']

votes = {candidate: 0 for candidate in candidates}

while True:
    vote = input("Введите имя кандидата, за которого голосуете: ")
    if vote in candidates:
        votes[vote] += 1
    else:
        print("Вы ввели некорректное имя кандидата.")
    more_votes = [candidate for candidate in candidates if votes[candidate] == max(votes.values())]
    if len(more_votes) == 1:
        winner = more_votes[0]
        break
    else:
        winner = sorted(more_votes, key=len)[0]

print("Победитель выборов: ", winner)
print("Количество голосов: ", votes[winner])


# Task 2
class MainClass:
    def __init__(self, text):
        self.text_field = text

    def set_text(self, text=None):
        if text:
            self.text_field = text
        else:
            self.text_field = input("Enter text: ")


class ChildClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number_field = number


main_obj = MainClass("Hello, world!")
print(main_obj.text_field)

main_obj.set_text()
print(main_obj.text_field)

child_obj = ChildClass("Text", 42)
print(child_obj.text_field)
print(child_obj.number_field)


# Task 3
class MainClass:
    def __init__(self, text):
        self.text = text

    def setText(self, text=None):
        if text is not None:
            self.text = text
        else:
            self.text = input("Enter text: ")

    def getClassName(self):
        return "MainClass"


class ChildClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number = number

    def setNumber(self, number):
        self.number = number

    def getClassName(self):
        return "ChildClass"


main_obj = MainClass("Text from MainClass")
child_obj = ChildClass("Text from ChildClass", 10)

main_obj.setText("New text from MainClass")
child_obj.setText("New text from ChildClass")
child_obj.setNumber(20)

print(main_obj.text)
print(child_obj.text)
print(child_obj.number)
print(main_obj.getClassName())
print(child_obj.getClassName())



