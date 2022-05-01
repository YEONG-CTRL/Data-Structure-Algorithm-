#0,1,1,2,3,5,8,13,21,34.....
#각 값은 이전 두개의 값의 합

# 주어진 숫자 N에 해당하는 피보나치 수열 인덱스의 값 리턴 
# ex 8 -> 21

def fibo_iterative(index):
    lst = [0,1]
    for i in range(2,index+1):
        lst.append(lst[i-2]+lst[i-1]) #O(n)


    return lst[index]


def fibo_recursive(index):
    #base case = 0,1  
    #recursive case = 1보다 큰 모든 수 
    #base return = index, recursive return = recursive(인덱스-1) + recursive(인덱스-2) 
    if index < 2: # base 
        return index
    return fibo_recursive(index-1)+fibo_recursive(index-2) #exponential time 
    # index가 하나커질때마다, tree의 사이즈가 exponential하게 커짐
    # https://commons.wikimedia.org/wiki/File:Fibonacci_Tree_5.svg
    # 숫자 하나 늘때마다 저 트리가 하나씩 생기는거
    # 따라서 Big O는 O(2^n) : exponential time
    # readble 하지만 , 시간복잡도 매우 매우 안좋음


# print(fibo_recursive(8))
print(fibo_recursive(40))    #한 참 걸 림(시간 복잡도)
    

