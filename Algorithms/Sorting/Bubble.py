

numbers = [99,44,6,2,1,5,63,87,283,4,0]

def bubblesort(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(length-1):
            if arr[j] > arr[j+1]:
                # swap
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

print(bubblesort(numbers))