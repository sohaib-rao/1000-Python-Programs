def printArrayReverse(arr, n):
    if n == 0:
        return
    print(arr[n-1], end=" ")
    printArrayReverse(arr, n-1)
    
arr = [10, 20, 30, 40, 50]
n = len(arr)

printArrayReverse(arr, n)