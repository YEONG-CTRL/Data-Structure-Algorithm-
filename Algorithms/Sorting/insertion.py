
arr = [0,2,3,1,4,6,5,7,9,8,0]

def insertion(arr):
    length = len(arr)
    i = 1
    end = arr[0]
    while i < length:
        if arr[i] < end:
            x = arr.pop(i)
            for j in range(0,i):
                if x < arr[j]:
                    arr.insert(j,x)
                    break
        end = arr[i]
        i += 1
    return arr

print(insertion(arr))            
        