class Greeting:
    def morning(self):
        print("Good Morning")

    def _afternoon(self):
        print("Good Afternoon")

    def __night(self):
        print("Good Night")


greeting1 = Greeting()
greeting2 = Greeting()

greeting1.morning()
greeting1._afternoon()
greeting1._Greeting__night()
print(id(greeting1) == id(greeting2))  # False
