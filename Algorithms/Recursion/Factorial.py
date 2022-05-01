# 숫자의 Factorial 을 찾는 함수
# 하나는 recursive , 하나는 iterative

def find_factorial_recursive(number): 
    if number <=2: #base
        return number
    else:
        return number * find_factorial_recursive(number-1) #recursive  # O(n)
    

def find_factorial_iterative(number):
    num = 1 
    for i in range(1,number+1):  # O(n)
        num = num*i
    return num 
    

print(find_factorial_recursive(5))