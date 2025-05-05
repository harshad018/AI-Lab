def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr

def insertion_sort(arr):
    for i in range (1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#Reasoing
def apply_sorting(arr,method):
    if method == 'selection':
        print("Using Selection Sort")
        return selection_sort(arr)
    elif method == 'insertion':
        print("Using Insertion Sort")
        return insertion_sort(arr)
    elif method == 'bubble':
        print("Using Bubble Sort")
        return bubble_sort(arr)
    else:
        print("Invalid choice.Using default:Insertion sort")
        return insertion_sort(arr)

#Main Program
def main():
    user_input =  input("Enter numbers separated by space: ")
    arr = list(map(int,user_input.strip().split()))

    print("\n Choose the sorting method: ")
    print("1.Insertion Sort ")
    print("2.Selection Sort")
    print("3.Bubble Sort")

    ch = input("Enter your choice : ").strip().lower()

    print("\n original array : ",arr)
    sorted_arr = apply_sorting(arr.copy(),ch)
    print("Sorted array : ",sorted_arr)

if __name__ == "__main__":
    main()
