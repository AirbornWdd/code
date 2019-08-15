def quicksort(array):
    if len(array) <= 1:
        return array

    right = []
    left = []
    m = len(array) / 2
    middle = array[m]
    array = array[:m] + array[m+1:]
    for x in array:
        if x > middle:
            right.append(x)
        else:
            left.append(x)
    return quicksort(left) + [middle] + quicksort(right)

print(quicksort([3,1]))
