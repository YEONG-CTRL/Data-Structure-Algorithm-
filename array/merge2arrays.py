def mergeSortedArray(array1, array2):
    merged_array = []
    i = 0
    j = 0

    if len(array1) == 0 or len(array2) == 0:
        return a + b

    while i<len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            merged_array.append(array1[i])
            i += 1
        elif array2[j] < array1[i]:
            merged_array.append(array2[j])
            j += 1
    return merged_array+array1[i:] + array2[j:] 
    #먼저 소진된쪽은 사라지기에 중복돼서 더해질 걱정 X

a=[1,2,3,4,20]
b=[2,3,4,5,6,9,10,11]
x=mergeSortedArray(a,b)
print(x)


        
    
    