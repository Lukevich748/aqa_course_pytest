

class Calculator:

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def division(self, a, b):
        if b == 0:
            ZeroDivisionError("Division by zero is not allowed.")
        return a / b

    def multiplication(self, a, b):
        return a * b
