# 10.22.15
# import ipdb; ipdb.set_trace()

def binarySearch(array, search, low, high):
    print low,high
    mid = (low+high)/2
    if low > high:
        return None
    if search < array[mid]:
        return binarySearch(array,search,low,mid-1)
    elif search > array[mid]:
        return binarySearch(array,search,mid+1,high)
    else:
        return mid

def driver(array, search):
    print binarySearch(array, search, 0, len(array)-1)

if __name__ == '__main__':
    array = [1,2,4,6,7,8]
    search = 1
    driver(array, search)
