# -*- coding: utf-8 -*-
"""

Arrays and Strings

"""

'''

# Max Consecutive Ones

nums = [1,1,0,1,1,1]
corr_ans = str(3)

def findMaxConsecutiveOnes(nums):
    
    overall_max = 0
    curr_max = 0    # edge cases
    for n in nums:  # O(n)
        if n == 1:  # check if 1
            curr_max += 1 
            overall_max = max(curr_max, overall_max)
        else:
            curr_max = 0
        
    return overall_max

ans = str(findMaxConsecutiveOnes(nums))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Find Numbers with Even Number of Digits

nums = [12,345,2,6,7896]
corr_ans = str(2)

def findNumbers(nums):
    
    if len(nums) == 0:
        return 0
    
    total_even = 0
    for n in nums:
        if len(str(n)) % 2 == 0:
            total_even += 1
    
    return total_even

ans = str(findNumbers(nums))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Squares of a Sorted Array

nums = [-4,-1,0,3,10]
corr_ans = str([0,1,9,16,100])

def sortedSquares(nums):
    
    if not nums:
        return nums
    
    sorted_nums = []
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        if abs(nums[right]) >= abs(nums[left]):
            sorted_nums.append(nums[right]**2)
            right -= 1
        else:
            sorted_nums.append(nums[left]**2)
            left += 1
            
    return sorted_nums[::-1]

ans = str(sortedSquares(nums))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Duplicate Zeros

arr = [1,0,2,3,0,4,5,0]
corr_ans = str([1,0,0,2,3,0,0,4])

def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """

    n = 0 
    
    while n < len(arr):
        if arr[n] == 0:
            arr = arr[0:n+1] + [0] + arr[n+1:len(arr)-1]
            n += 2
        else:
            n += 1
        print(arr)
     
    return arr

ans = str(duplicateZeros(arr))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Remove Element

nums, val = [0,1,2,2,3,0,4,2], 2
corr_ans = str([0,1,3,0,4,'','',''])

nums, val = [3,2,2,3], 3
corr_ans = str([2,2,'',''])

def removeElement(nums, val):
    
    n = 0 
    
    while n < len(nums):
        if nums[n] == val:
            nums = nums[:n] + nums[n+1:] + ['']
        else:
            n += 1

    return nums

ans = str(removeElement(nums, val))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Check If N and Its Double Exist (1. Brute Force)

arr = [3,1,7,11]
corr_ans = str(False)
def checkIfExist(arr):
    
    exist = False
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[j] == arr[i] // 2 and arr[i] % 2 == 0) or arr[j] == 2*arr[i]:
                exist = True
                return exist
            
    return exist

ans = str(checkIfExist(arr))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Check If N and Its Double Exist (2. Set Lookup)

arr = [3,1,7,11]
corr_ans = str(False)

def checkIfExist(arr):
    
    exist = False
    
    exist = False
    seen = set()
    for num in arr:
        if (num // 2 in seen and num % 2 == 0) or (num*2 in seen):
            exist = True
            return exist
        seen.add(num)
            
    return exist

ans = str(checkIfExist(arr))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Check If N and Its Double Exist (3. Frequency Map)

arr = [3,1,7,11]
corr_ans = str(False)

def checkIfExist(arr):
    freq = {}
    exist = False
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    exist = False
    for num in arr:
        if num != 0 and 2 * num in freq:
            exist = True
            return exist
        if num == 0 and freq[num] > 1:
            exist = True
            return exist
            
    return exist

ans = str(checkIfExist(arr))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Valid Mountain Array

arr = [0,3,2,1]
corr_ans = str(True)

def validMountainArray(arr):
    
    if len(arr) <= 2 or arr[0] >= arr[1]:  # initial up check and min len(arr)
        return False
    
    index = 1
    while arr[index+1] > arr[index] and index < len(arr) - 2:  # up conditon
        index += 1
        
    while arr[index+1] < arr[index] and index < len(arr) - 2:  # down condition
        index += 1
    
    if arr[index+1] < arr[index] and index == len(arr) - 2:    # final index check 
        return True

ans = str(validMountainArray(arr))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Replace Elements with Greatest Element on Right Side (missed temp_val which was needed...)

arr = [17,18,5,4,6,1]
corr_ans = str([18,6,6,6,1,-1])

def replaceElements(arr):
    
    if len(arr) == 1:
        return [-1]
    max_val = -1
    
    for i in range(len(arr) - 1, -1, -1):
        # print(i, arr[i], max_val)
        temp_val = arr[i]
        arr[i] = max_val
        if temp_val > max_val:
            max_val = temp_val
            
    return arr

ans = str(replaceElements(arr))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Remove Duplicates from Sorted Array

nums = [0,0,1,1,1,2,2,3,3,4]
corr_ans = str([0,1,2,3,4,"","","","",""]) + ", " + str(5)

def removeDuplicates(nums):
    
    size = len(nums)
    write_index = 1
    for i in range(1, size):
        if nums[i-1] != nums[i]:
            nums[write_index] = nums[i]
            write_index += 1
    return nums, write_index

ans1 = str(removeDuplicates(nums)[0])
ans2 = str(removeDuplicates(nums)[1])
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans1 + ", " + ans2 + ". " + "Answers Match!", corr_ans == ans1 + ", " + ans2)

# Move Zeroes

nums = [0,1,0,3,12]
corr_ans = str([1,3,12,0,0])

def moveZeroes(nums):
    
    if len(nums) == 1:
        return nums
    
    size = len(nums)
    write_index = 0
    for i in range(0, size):
        if nums[i] != 0:
            nums[write_index] = nums[i]
            write_index += 1
    for i in range(write_index, size):
        nums[i] = 0

    return nums

ans = str(moveZeroes(nums))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Sort Array By Parity

nums = [3,1,2,4]
corr_ans = str([4,2,1,3])

def sortArrayByParity(nums):

    size = len(nums)
    if len(nums) == 0:
        return nums
    
    l = 0
    r = size - 1
    
    while l < r:
        if nums[l] % 2 == 1 and nums[r] % 2 == 0:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l += 1
            r -= 1
        elif nums[l] % 2 == 0 and nums[r] % 2 == 0:
            l += 1
        elif nums[l] % 2 == 1 and nums[r] % 2 == 1:
            r -= 1
        else:
            l += 1
            r -= 1
            
    return nums

ans = str(sortArrayByParity(nums))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

'''

# Max Consecutive Ones II

nums = [1,0,1,1,0,1]
corr_ans = str(4)

def findMaxConsecutiveOnes(nums):

    i = 0
    j = 0 
    k = 1
    max_ones = 0 
    hash_dict = {0: 0}
    while j < len(nums):
        hash_dict[nums[j]] = 1 if nums[j] not in hash_dict else hash_dict[nums[j]] + 1
        if hash_dict[0] <= k:            # equal as long as were adding new letters
            max_ones = max(max_ones, j - i + 1)
        else:            # less than window length if letter occurs twice 
            while hash_dict[0] > k:      # loop until hash map size is gt or equal to window length
                hash_dict[nums[i]] -= 1   # de-increment letter at beginning of the window
                i += 1                    # slide beginning of window forward
        j += 1 
            
    return max_ones

ans = str(findMaxConsecutiveOnes(nums))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Next Problem







# Next Problem







# Next Problem







# Next Problem







# Next Problem







# Next Problem







# Next Problem