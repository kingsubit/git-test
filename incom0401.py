class Animal:
     def sound(self):
          print("동물이 소리를 냅니다.")

class Dog(Animal):
     def sound(self):
          print("멍멍!")

class Cat(Animal):
     def sound(self):
          print("야옹!")

a=Animal()
d=Dog()
c=Cat()

a.sound()
d.sound()
c.sound()

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second
        
calc = FourCal(4, 2)
print(calc.add())  # 6
print(calc.sub())  # 2

class MoreFourCal(FourCal):
    def pow(self): #두 수의 거듭제곱 메소드
        return self.first ** self.second

m = MoreFourCal(3, 2)
print(m.pow()) 
print(m.add()) #상속받은 메소드 잘 작동?

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return "0으로 나눌 수 없습니다."
        return self.first / self.second
        
a = SafeFourCal(4,0)
a.div()
print(a.div())

class Family:
    lastname = "김"  # 클래스 변수

print(Family.lastname)  # 김

a = Family()
b = Family()
print(a.lastname)
print(b.lastname) 

class BankAccount:
    def __init__ (self,amount):
        self.amount=amount
        