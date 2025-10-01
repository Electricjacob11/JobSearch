def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


list = quicksort([3,6,8,10,1,2,1])

for i in range(len(list)-1):
    if list[i] + 1 != list[i+1]:
        print(f"Missing number between {list[i]} and {list[i+1]}: {list[i]+1}")