def add_to_80(n):
    print("long time")
    return n+80

# cache = {} # global영역에 있는 것을  피하기 위해 함수 안에 있는게 더 좋음
def memoized_add_to_80():
    cache = {} 
    def memoized(n): #클로저 사용
        if n in cache: # 중복 계산x
            return cache[n] # 바깥쪽 함수의 지역변수에 접근
        else:
            print("long time")
            cache[n] = n + 80
            return cache[n]
    return memoized

vmemo =memoized_add_to_80()
#memoized_add_to_80함수는 cache변수를 만들고 memoized함수를 return

print(1, vmemo(5))
print(2, vmemo(5))