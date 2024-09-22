def bubble_sort(arr):
    n = len(arr)
    print(n)
    for i in range(n):
        print(i)
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example list
lst = [1, 5, 2, 6, 9, 13, 4]
bubble_sort(lst)
print("Sorted list is:", lst)
