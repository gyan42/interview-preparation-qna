# Python program for implementation of Insertion Sort
"""
Time Complexity
Best O(n)
Worst O(n^2)
Average O(n^2)
Space Complexity O(1)
Stability Yes

"""
# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])