def mergesort(arr):
    if len(arr) == 1:
        return arr
    length = len(arr)
    mid    = length//2
    left   = arr[:mid]
    right  = arr[mid:]

    return merge(mergesort(left),mergesort(right))

def merge(left,right):
    result = []
    leftindex  = 0
    rightindex = 0
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            result.append(left[leftindex])
            leftindex += 1
        else:
            result.append(right[rightindex])
            rightindex += 1
    return result + left[leftindex:] + right[rightindex:]

x= mergesort([99,44,6,2,1,5,63,87,283,4,0])
print(x)