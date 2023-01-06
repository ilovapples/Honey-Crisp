def isOdd(num):
    if num%2 == 0:
        return False
    else:
        return True

def isEven(num):
    if num%2 == 0:
        return True
    else:
        return False

def mean(nums: list):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)

def mode(nums: list):
    frequencies = {}
    for num in nums:
        frequencies[str(num)] = nums.count(num)
    
    return int(max(frequencies, key=frequencies.get))

def median(nums: list):
    nums.sort()
    sortedNums = nums.copy()
    if isOdd(len(nums)):
        return sortedNums[int(len(nums)/2+0.5)-1]
    else:
        middleNums = []
        middleNums.append(sortedNums[int(len(nums)/2)-1])
        middleNums.append(sortedNums[int(len(nums)/2+1)-1])
        return mean(middleNums)

nums = [1, 1, 3, 5, 7, 9, 9, 10, 15]
print("Median: %s\nMode: %s\nMean: %s" % (median(nums), mode(nums), mean(nums)))