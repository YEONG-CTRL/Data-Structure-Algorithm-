arr = [5,9,1,2,7,3,8,2]

def selectionsort(array):
    count = 0
    for i in range(len(array)-1):
        minn = array[i]
        index = i
        for j in range(i+1, len(array)):
            count += 1
            if array[j] < minn :
                index = j
                minn = array[j]
        if index != i:
            array[i] , array[index] = array[index], array[i]
    
    return array

print(selectionsort(arr))