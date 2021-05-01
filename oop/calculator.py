class Claculator:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second

    @staticmethod
    def execute():
        calc = Claculator(int(input("first number")), int(input("second number")))
        print(f'첫번째수:{calc.first}')
        print(f'두번째수:{calc.second}')
        print(f'덧셈:{calc.sum()}')
        print(f'뺄셈:{calc.sub()}')
        print(f'곱셈:{calc.mul()}')
        print(f'나눗셈:{calc.div()}')

if __name__ == '__main__':
    Claculator.execute()
