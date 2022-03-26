class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.reset = 0

    def adder(self):
        return self.num1 + self.num2

    def subtractor(self):
        return self.num1 - self.num2

    def multiplier(self):
        return self.num1 * self.num2

    def divider(self):
        return self.num1 / self.num2

    def clear(self):
        return self.reset


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
calc = Calculator(a, b)

print("Add: ", calc.adder())
print("Subtract: ", calc.subtractor())
print("Multiplication: ", calc.multiplier())
print("Division: ", calc.divider())
print("Clear", calc.clear())