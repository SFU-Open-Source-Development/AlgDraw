# merge sort is a divide and conquer sorting algorithm 
# it recursively divides the array in half and calls the merge function on it

def MergeSort(array, start, end):
    # start and end refer to the indexes that mark the beginning and end of the array that we are trying to sort
    if start >= end:
        return
    
    midpoint = (start + end)//2 
    MergeSort (array, start, midpoint)
    MergeSort (array, midpoint+1, end)
    merge (array, start, end, midpoint)


# merge function makes copies of the two smaller arrays given to the funciton
# copies the elements in a sorted manner back into the original array
def merge (array, start, end, midpoint):
    # first, we need to make copies of the two sub arrays
    left_array = array[start:midpoint+1]
    right_array = array[midpoint+1:end+1]

    left_array_index = 0
    right_array_index = 0
    sorted_index = start
    
    while left_array_index < len(left_array) and right_array_index < len(right_array):
        # goes through elements of both subarray one by one
        # copies the smaller element between into the sorted array

        if left_array[left_array_index] <= right_array[right_array_index]:
            array[sorted_index] = left_array[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_array[right_array_index]
            right_array_index += 1
        
        # regardless of subarray indexes, sorted_index should increase
        sorted_index += 1
    
    # if elements of either subarary run out, copy remaining elements of other subarray in sorted array
    # subarrays are assumed to be sorted due to recursion

    while left_array_index < len(left_array):
        array[sorted_index] = left_array[left_array_index]
        sorted_index += 1
        left_array_index += 1
    
    while right_array_index < len(right_array):
        array[sorted_index] = right_array[right_array_index]
        sorted_index += 1
        right_array_index += 1
