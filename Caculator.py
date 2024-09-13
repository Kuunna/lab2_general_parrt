class CCaculator:
    def __init__(self, x, y):
        self.x = 3
        self.y = 4
    def Sum(self):
        return self.x + self.y
    def Mutiple(self):
        return self.x * self.y
MyCalc = CCaculator(3, 2) 

print(MyCalc.Sum())
print(MyCalc.Mutiple())
print(1+2+3)