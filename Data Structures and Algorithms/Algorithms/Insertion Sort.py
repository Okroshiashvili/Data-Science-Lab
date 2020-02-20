


"""

Insertion sort is the method to sort an array.

In insertion sort we divide an array into two parts: sorted part and
unsorted part. Every time we select the first value from the unsorted part and
find its position in sorted part and place it there.


"""


def insertion_sort(arr):
    # Insertion sort is composed of two loops
    # One is outer loop and second is inner loop
    # I'll use for loop as an outer loop and
    # while loop as an inner loop
    for i in range(1, len(arr)):
        value = arr[i]
        # Inner loop
        j = i
        while (j > 0 and arr[j-1] > value):
            arr[j] = arr[j-1]
            j = j - 1
            
        arr[j] = value


# Test the code
array = [30, 44, 67, 5, 8, 9, 53]
            
# Let sort this array
insertion_sort(array)
# Insertion sort did in-place sort
print(array)

