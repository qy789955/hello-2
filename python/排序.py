def bubble_sort(array):
    if len(array) <2:
        return array
    else:
        num = 0
        for j in range(len(array)-1):
            for i in range(len(array)-1-j):
                num += 1
                if array[i] > array[i+1]:
                    mid = array[i+1]
                    array[i+1], array[i] = array[i], mid 
            print(array)
    print(num)
    return array

array_0 = [12, 23, 54, 32, 11, 76, 5, 73]
print(bubble_sort(array_0))