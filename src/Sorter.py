#Class Sorter, allows us to create an instance of a sorter, and then sort different arrays of data

class Sorter:
    def __init__(self):
        #Nothing important really happens other than initializing the Sorter
        pass


    def BubbleSort(self, array):

        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                firstNum = array[j]
                secondNum = array[j + 1]

                if secondNum < firstNum:
                    array[j], array[j + 1] = secondNum, firstNum
        return array


    def InsertionSort (self, array):

        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array


    def MergeSort(self, array, start, end):

        # start and end refer to the indexes that mark the beginning and end of the array that we are trying to sort
        if start >= end:
            return

        midpoint = (start + end) // 2
        self.MergeSort(array, start, midpoint)
        self.MergeSort(array, midpoint + 1, end)
        self.merge(array, start, end, midpoint)
        return array

    # merge function makes copies of the two smaller arrays given to the funciton
    # copies the elements in a sorted manner back into the original array
    def merge(self, array, start, end, midpoint):
        # first, we need to make copies of the two sub arrays
        left_array = array[start:midpoint + 1]
        right_array = array[midpoint + 1:end + 1]

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

    def SelectionSort (self, array):
        pass


