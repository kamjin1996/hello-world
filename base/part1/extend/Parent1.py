class Parent1:
    "父类1"

    def __str__(self):
        return "Parent1(%s)" % self.parent1Value

    def __init__(self):
        print("Parent1 init")
        self.parent1Value = 1

    def parent1Method(self):
        print("parent1的函数")

    def setValueTo10(self):
        self.parent1Value = 10

    def getValue(self):
        return self.parent1Value
