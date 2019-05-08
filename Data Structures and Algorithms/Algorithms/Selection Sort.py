"""
Created on Wed May  8 2019

@author: Nodar Okroshiashvili
"""




"""

In selection sort we select the smallest value from an array and swap it
with the first value of the unsorted part.


"""


def selection_sort(arr):
    for i in range(0,len(arr)-1):
        min_value_index = i
        for j in range(i+1, len(arr)):
            if (arr[min_value_index] > arr[j]):
                min_value_index = j
        
        temp_value = arr[i]
        arr[i] = arr[min_value_index]
        arr[min_value_index] = temp_value


# Let test the code
array = [90, 35, 60, 7, 2, 3, 89]
            
# Sort the array
selection_sort(array)         
# Print sorted array
print(array)


