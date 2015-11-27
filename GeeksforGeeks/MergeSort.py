# 10/18/15
import pdb, traceback, sys, code

def mergeSort(array):
    if len(array) > 1:
        middle = len(array)/2
        array_left = array[:middle]
        array_right = array[middle:]

        mergeSort(array_left)
        mergeSort(array_right)

        i = 0
        j = 0
        k = 0

        while i < len(array_left) and j < len(array_right):
            if array_left[i] <= array_right[j]:
                array[k] = array_left[i]
                k += 1
                i += 1
            else:
                array[k] = array_right[j]
                k += 1
                j += 1

        while i < len(array_left):
            array[k] = array_left[i]
            k += 1
            i += 1

        while j < len(array_right):
            array[k] = array_right[j]
            k += 1
            j += 1
        print array

def main():
    # array = [1,5,6,18,3,-1,4,3,1,2]
    array = [19,-1,3,1]
    mergeSort(array)
    print array

if __name__ == '__main__':
    main()
