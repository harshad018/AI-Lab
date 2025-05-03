def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
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
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Example usage
if __name__ == "__main__":
    # Get input from user
    nums = input("Enter numbers separated by spaces: ")
    arr = list(map(int, nums.strip().split()))
    
    print("Original array:", arr)
    
    # Choose sorting method
    print("\nChoose sorting method:")
    print("1. Bubble sort")
    print("2. Selection sort")
    print("3. Insertion sort")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        print("Bubble sorted:", bubble_sort(arr.copy()))
    elif choice == "2":
        print("Selection sorted:", selection_sort(arr.copy()))
    elif choice == "3":
        print("Insertion sorted:", insertion_sort(arr.copy()))
    else:
        print("Invalid choice")