class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        print(self.num1 + self.num2)
    
    def sub(self):
        print(self.num1 - self.num2)

    def mul(self):
        print(self.num1 * self.num2)
        
    def div(self):
        try:
            result = int(self.num1 / self.num2)
        except:
            result = 0
        finally:
            print(result)

    def mod(self):
        print(self.num1 % self.num2)

num1, num2 = map(int, input().split())

cal = calculator(num1, num2)

cal.add()
cal.sub()
cal.mul()
cal.div()
cal.mod()