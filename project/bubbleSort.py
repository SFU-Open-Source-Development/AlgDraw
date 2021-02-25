###################
#  Bubble Sort
#
#  24/02/2021
###################

def bubbleSort(array):
    '''

    :input parameter: list of numbers
    :return: sorted list in ascending order
    '''
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            firstNum = array[j]
            secondNum = array[j + 1]

            if secondNum < firstNum:
                array[j], array[j + 1] = secondNum, firstNum


test_list = [20,1,-2,60,7]

print("\noriginal list\n",test_list)

bubbleSort(test_list)

print("\nsorted list",test_list)
