calculation_old = 0
def fibonacci(n): # O(2^n) -> 매우 느림
    global calculation_old
    calculation_old += 1
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(15))
print(calculation_old , "times")

# 다이내믹 프로그래밍으로 이를 O(n)까지 줄일 수 있음
calculation = 0

def fibonacci_dyna():
    cache = {}
    def fib(n):
        global calculation
        calculation += 1
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fib(n-1) + fib(n-2)
                return cache[n]
    return fib

fasterfib = fibonacci_dyna()
print(fasterfib(15))
print(calculation ,"times")