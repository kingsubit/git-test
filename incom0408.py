#팩토리얼
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))  # 5! = 5*4*3*2*1 = 120 출력