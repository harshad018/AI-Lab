

def bubble_sort(arr):

    n = len(arr)

    for i in range( n ):
        for j in range(n-1-i):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

def selection_sort(arr):

    n = len(arr)

    for i in range(n):
        min_pos = i

        for j in range(i+1, n):

            if arr[j] < arr[min_pos]:
                min_pos = j

        arr[i], arr[min_pos] = arr[min_pos], arr[i]

    return arr


def insertion_sort(arr):

    for i in range(1 , len(arr)):
        key = arr[i]
        j = i -1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]

            j -= 1
        arr[j+1] = key

    return arr
