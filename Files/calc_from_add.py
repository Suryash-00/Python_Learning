from addition import Addition

class Calculator:

    @classmethod
    def add(cls, num1, num2):
        print(Addition.add(num1, num2))

    @classmethod
    def subtract(cls, num1, num2):
        print(Addition.add(num1, -num2))

    @classmethod
    def multiply(cls, num1, num2):
        num0 = num1
        for num in range(num2 - 1):
            num1 = Addition.add(num1, num0)

        print(num1)

    @classmethod
    def divide(cls, num1, num2):
        c = 0
        while num1 != 0:
            num1 = Addition.add(num1, -num2)
            c = c + 1
        print(c)

cl=Calculator()

cl.multiply(10, 5)