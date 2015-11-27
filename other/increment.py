# 10/18/15
# [1,2,4] -> [1,2,5]
def increment(numbers):
    for i in range(0, len(numbers)):
        j = len(numbers)-i-1
        numbers[j] += 1
        if numbers[j]%10 == 0:
            numbers[j] = 0
            if j == 0:
                newNumbers = [0 for i in range(len(numbers))]
                newNumbers.insert(0, 1)
                return newNumbers
        else:
            break
    return numbers

if __name__ == '__main__':
    print increment([1,2,4])
    print increment([1,2,9])
    print increment([9,9])
