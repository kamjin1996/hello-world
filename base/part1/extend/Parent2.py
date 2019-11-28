class Parent2:
    "父类2"

    def __str__(self):
        return "Parent2(%s)" % self.parent2Value

    def __init__(self):
        print("Parent2 init")
        self.parent2Value = 1

    def parent1Method(self):
        print("parent2的函数")

    def setValueTo20(self):
        self.parent1Value = 20

    def getValue(self):
        return self.parent1Value
