#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 11:44:52 2025

@author: LiamBiam
"""

##########################################
############### Hash-Table ###############
##########################################

# Design HashSet... Basic Hashset (Good Enough for Problem 1)

class Basic_MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            print(self.hashset)
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hashset
    
# Design HashSet... Proper Multiplicitave Hashset (More Effective for Problem 1)

class MyHashSet:
    
    '''
    
    Using Multiplicative Hash-Set and adding eval_hash to ensure 
    proper bucketing to improve time complexity of algorithm. T
    
    The basic version of this that is accepted for this problem 
    uses contains method to see if key in array for add, remove, 
    and also obviously contains, which are the core operations 
    of the class. The improved implementation uses eval hash to
    effectively attribute a unique number and bit-wise operations
    to better check if the hash-set contains a key or not. (check pics)
    
    Space Complexity is worse bit time complexity is better
    
    '''
    
    def eval_hash(self, key):
        return ((key*1122339) & (1<<20) - 1)>>5
    
    def __init__(self):
        self.hashset = [[] for _ in range(1<<15)]

    def add(self, key: int) -> None:
        num = self.eval_hash(key)
        if key not in self.hashset[num]:
            self.hashset[num].append(key)

    def remove(self, key: int) -> None:
        num = self.eval_hash(key)
        if key in self.hashset[num]:
            self.hashset[num].remove(key)

    def contains(self, key: int) -> bool:
        num = self.eval_hash(key)
        return key in self.hashset[num]
    
# Design HashMap... using dictionaries (the easy way)
    
class Basic_MyHashMap:

    def __init__(self):
        self.hashset = {}

    def put(self, key: int, value: int) -> None:
        self.hashset[key] = value

    def get(self, key: int) -> int:
        if key not in self.hashset:
            return -1
        return self.hashset[key]

    def remove(self, key: int) -> None:
        if key in self.hashset:
            del self.hashset[key]
    
# Design HashMap... using a list of lists (the hard C++ and Java way)
    
class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break

        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]
                
class MyHashMap:

    def __init__(self):
        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]


    def put(self, key, value):
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)


    def get(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)


    def remove(self, key):
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)

# Contains Duplicate

nums = [1,2,3,1]
corr_ans = str(True)

def containsDuplicate(nums):
    
    hashset = {}
    for n in nums:
        if n not in hashset:
            hashset[n] = 1
        else:
            return True
            
    return False

ans = str(containsDuplicate(nums))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Single Number (Dictionary Method)

nums = [4,1,2,1,2]
corr_ans = str(4)

def dict_singleNumber(nums):
    
    hashset = {}
    for n in nums:
        if n not in hashset:
            hashset[n] = 1
        else:
            hashset[n] += 1
    for key, value in hashset.items():
        if value == 1:
            return key

ans = str(dict_singleNumber(nums))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Single Number (List Method for C++ and Java)

nums = [4,1,2,1,2]
corr_ans = str(4)

def singleNumber(nums):
    
    '''
    
    This takes advantage of the fact we know ahead of time
    that theres exactly two occurances of each number except
    for the case where there's one occurance. So we append(n)
    and remove(n) to fill then get rid of all numbers that
    occur twice, and pop() the last remaining list element at the end
    
    '''
    
    hashset = []
    for n in nums:
        if n not in hashset:
            hashset.append(n)
        else:
            hashset.remove(n)
    return hashset.pop()

ans = str(singleNumber(nums))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Intersection of Two Arrarys

nums1 = [4,7,9,7,6,7]
nums2 = [5,0,0,6,1,6,2,2,4]
corr_ans = str(sorted([6,4]))

def intersection(nums1, nums2):
    
    '''
    
    This could work in either order (doesn't matter if we interchange
    nums1 and nums2) because we're looking for the intersection.
    
    Start by finding what exists in nums1, then we look through nums2
    to put together the list of all numbers that exist in both lists.
    
    1) Take note of whats in nums1 by setting hashset[n] = 1 (could be
    any other method of initialization, but assigning a 1 to key works)
    
    2) For whatevers in hashset after going through nums1, append that
    number to intersection, but don't duplicate it, so part of the if
    condition is that the number is not already in intersection.
    
    '''
    
    hashset = {}
    for n in nums1:
        if n not in hashset:
            hashset[n] = 1
            
    intersection = []
    for n in nums2:
        if n in hashset and n not in intersection:
            intersection.append(n)
            
    return intersection

ans = str(sorted(intersection(nums1, nums2)))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Happy Number (Recursive Method)

n = 19
corr_ans = str(True)

def isHappy(n):
    
    '''
    
    Why do we need to hash you may ask.
    Silly Padwon. Because of cycles. Yes cycles exist where the 
    math will take you back to an existing number, an infinite loop.
    
    Now the math part. This part is annoying. This approach will
    take the digits of the number, which will be done by converting 
    the returned number to a string, then splitting the numbers, then
    converting back to integers and squaring the numbers, adding them
    all together to get the next number. 
    
    Now the while loop or recursion part will first add the number to 
    the hashset, so we don't infinite loop in circles, do the math part,
    then return True if we reach happy number 1, or return False if we 
    get 3 or less or see the number reoccuring in the hashset.
    
    '''
    
    hashset = {}
    
    def helper(num):

        hashset[num] = 1

        number = 0
        for s in list(str(num)):
            number += (int(s))**2

        if number == 1:
            return True

        if number < 4 or number in hashset:
            return False

        return helper(number)
    
    return helper(n)

ans = str(isHappy(n))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Two Sum (HashMap)

nums = [2,7,11,15]
target = 9
corr_ans = str([0,1])

def twoSum(nums, target):

    hashmap = {i:n for i, n in enumerate(nums)}
    nums = sorted(nums)
    
    for i in range(len(nums)):
        one_diff = target - hashmap[i]
        for j in range(i + 1, len(nums)):
            if one_diff - hashmap[j] == 0:
                return [i, j]

ans = str(twoSum(nums, target))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Isomorphic Strings

s = "paper"
t = "title"

corr_ans = str(True)

def isIsomorphic(s, t):
    
    '''
    
    Trick is to see if characters repeat in the same locations.
    Code will be to see if the HashMaps are the same after.
    
    Ex) s is paper, and t is title
    s_hashmap = {0:0, 1:1, 2:0, 3:2, 4:3} 
    s_hashset = {'p':0,'a':1,'e':2,'r':3}
    t_hashmap = {0:0, 1:1, 2:0, 3:2, 4:3} 
    t_hashset = {'t':0,'i':1,'l':2,'e':3}
    
    ASCII is a long set of characters, so I need to have a reference
    hashset to know if a character is reoccuring, and what index to allocate 
    it to. Whenever I encounter a character another time I will increment 
    the number of repeats so values correspond between the hashmap and hashset
    
    '''
    
    s_hashmap = {}
    s_hashset = {}
    t_hashmap = {}
    t_hashset = {}
    
    s_repeats = 0
    for i in range(len(s)):
        if s[i] in s_hashset:
            s_hashmap[i] = s_hashset[s[i]]
            s_repeats += 1
        else:
            s_hashset[s[i]] = i - s_repeats
            s_hashmap[i] = i - s_repeats
    
    t_repeats = 0
    for i in range(len(t)):
        if t[i] in t_hashset:
            t_hashmap[i] = t_hashset[t[i]]
            t_repeats += 1
        else:
            t_hashset[t[i]] = i - t_repeats
            t_hashmap[i] = i - t_repeats

    return s_hashmap == t_hashmap

ans = str(isIsomorphic(s, t))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Minimum Index Sum of Two Lists

list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
corr_ans = str(["sad","happy"])

# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["KFC","Shogun","Burger King"]
# corr_ans = str(["Shogun"])

def findRestaurant(list1, list2):
    
    '''
    
    1) need to determine common strings
    2) need to determine index sum for indicies in list1 and list2 words
    3) return all words with indicies that sum to min_sum
    
    '''
    
    def inBothLists(l1, l2):
        
        common_strings = []
        
        for word in l1:
            if word in l2:
                common_strings.append(word)
        
        return common_strings
    
    if len(list1) > len(list2):
        common_strings =  inBothLists(list1, list2)       
    else:
        common_strings =  inBothLists(list2, list1)   

    common_hashmap = {word:None for word in common_strings}
    
    for i, word in enumerate(list1):
        if word in common_strings:
            common_hashmap[word] = i

    min_sum = 10**6
    for j, word in enumerate(list2):
        if word in common_strings:
            common_hashmap[word] += j
            min_sum = min(min_sum, common_hashmap[word])
            
    ans = []
    for word in common_hashmap:
        if common_hashmap[word] == min_sum:
            ans.append(word)

    return ans

ans = str(findRestaurant(list1, list2))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# First Unique Character in a String

s = "loveleetcode"
corr_ans = str(2)

def firstUniqChar(s):
    
    hashmap = {}
    
    for i, string in enumerate(s):
        if string not in hashmap:
            hashmap[string] = [1, i]
        else:
            hashmap[string][0] += 1
            
    for string in hashmap:
        if hashmap[string][0] == 1:
            return hashmap[string][1]
        
    return -1

ans = str(firstUniqChar(s))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect")

# Intersection of Two Arrays II

nums1 = [1,2,2,1]
nums2 = [2,2]
corr_ans = str([2,2])

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
corr_ans = str([9, 4])

def intersect(nums1, nums2):

    '''
    
    Need to determine which numbers and how many interect both lists
    
    1) Build HashMap of each nums1 and nums2 lists with key:count
    2) Go through the unique elements of nums1 + nums2 and to get the
       interection, we append the minimum of each count in both HashMaps.
    
    
    '''
    
    hashmap1 = {}
    hashmap2 = {}
    
    for n in nums1:
        if n not in hashmap1:
            hashmap1[n] = 1
        else:
            hashmap1[n] += 1
    
    for n in nums2:
        if n not in hashmap2:
            hashmap2[n] = 1
        else:
            hashmap2[n] += 1
            
    intersection = []
    for n in list(set(nums1 + nums2)):
        if n in hashmap1 and n in hashmap2:
            for i in range(min(hashmap1[n], hashmap2[n])):
                intersection.append(n)
                
    return intersection

ans = str(intersect(nums1, nums2))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect... Correct Answer is " + corr_ans + ", your answer was " + ans)

# Contains Duplicate II

nums = [1,2,3,1]
k = 3
corr_ans = str(True)

nums = [1,2,3,1,2,3]
k = 2
corr_ans = str(False)

# nums = [99,99]
# k = 2
# corr_ans = str(True)

def containsNearbyDuplicate(nums, k):

    '''
    
    Just move through the list removing hashset elements when the 
    hashset size exceeds k. Return True if num is in the hashset.
    If theres never any duplicates within k indicies away, Return False.
    
    '''
    
    hashset = {}
    for i in range(len(nums)):
        if nums[i] in hashset:
            return True
        hashset[nums[i]] = 1
        if len(hashset) > k:
            del hashset[nums[i-k]]

    return False

ans = str(containsNearbyDuplicate(nums, k))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect... Correct Answer is " + corr_ans + ", your answer was " + ans)

# Group Anagrams (Methodical Solution)

strs = ["eat","tea","tan","ate","nat","bat","",""]
corr_ans = str([["bat"],["nat","tan"],["ate","eat","tea"],["",""]])

def groupAnagrams(strs):
    
    '''
    
    Goal is to organize the hashmaps datastructure so we get;
    
    [[0, 'eat', {'e': 1, 'a': 1, 't': 1}],
     [1, 'tea', {'t': 1, 'e': 1, 'a': 1}],
     [2, 'tan', {'t': 1, 'a': 1, 'n': 1}],
     [3, 'ate', {'a': 1, 't': 1, 'e': 1}],
     [4, 'nat', {'n': 1, 'a': 1, 't': 1}],
     [5, 'bat', {'b': 1, 'a': 1, 't': 1}],
     [6, '', {}],
     [7, '', {}]]
    
    with strs = ["eat","tea","tan","ate","nat","bat","",""]
    
    '''
    
    hashmaps = []
    for i, string in enumerate(strs):
        hashmaps.append([i,string,{}])
        for s in string:
            if s not in hashmaps[i][2]:
                hashmaps[i][2][s] = 1
            else:
                hashmaps[i][2][s] += 1

    from collections import defaultdict
                
    grouped = defaultdict(list)
        
    for _, word, char_map in hashmaps:
        key = frozenset(char_map.items())  # hashable and ignores order
        grouped[key].append(word)

    list_of_lists = list(grouped.values())
    return list_of_lists

ans = str(groupAnagrams(strs))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect... Correct Answer is " + corr_ans + ", your answer was " + ans)

# Group Anagrams (Clever String Choice Solution)

strs = ["eat","tea","tan","ate","nat","bat","",""]
corr_ans = str([["bat"],["nat","tan"],["ate","eat","tea"],["",""]])

def groupAnagrams(strs):
    
    # take advantage of the fact tuple can be used as a key

    from collections import defaultdict
    grouped = defaultdict(list)
    for string in strs:
        count = [0] * 26
        for s in string:
            count[ord(s)-ord('a')] += 1
        grouped[tuple(count)].append(string)
    return list(grouped.values())

ans = str(groupAnagrams(strs))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect... Correct Answer is " + corr_ans + ", your answer was " + ans)

# Group Shifted Strings

strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
corr_ans = str([["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]])

def groupStrings(strings):
    
    '''
    
    To solve this efficiently, we need to take advantage of the facts;
    
    1) Utilize knowledge that ord() and chr() operations are inverse of each other.
    --> chr returns the character given the ordinal unicode point
    2) shift_letter returns letters shifted back to the 'a' location
    3) get_hash will return the whole string shifted back to 'a' location
                                                              
    Finally we loop through the strings, shifting them each back just for the key 
    so we can buildup our hashmap with lists of grouped strings, with the list of 
    unmodified strings being the output we return using list(grouped.values())
    
    grouped = {'abc': ['abc', 'bcd', 'xyz'], 'acef': ['acef'], 
               'az': ['az', 'ba'], 'a': ['a', 'z']}
    
    '''
    
    def shift_letter(letter, shift):
        return chr((ord(letter) - shift) % 26 + ord('a'))

    def get_hash(string):
        shift = ord(string[0])
        return ''.join(shift_letter(letter, shift) for letter in string)

    from collections import defaultdict
    grouped = defaultdict(list)
    for string in strings:
        hash_key = get_hash(string)
        grouped[hash_key].append(string)

    return list(grouped.values())

ans = str(groupStrings(strings))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect... Correct Answer is " + corr_ans + ", your answer was " + ans)

# Valid Sudoku (the normal way, barely using the hashmap concept)

board = (
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

corr_ans = str(True)

def isValidSudoku(board):
    
    '''
    
    row and column wise repeat number loops are simple enough;
    just loop through all rows with board[i][j] and columns with board[j][i]
    
    the boxes are something else, the best I could get was this;
    
    boxes = 
    [['5', '3', '.'],
     ['6', '.', '.'],
     ['.', '9', '8'],
     ['.', '7', '.'],
     ['1', '9', '5'],
     ['.', '.', '.'],
     ['.', '.', '.'],
     ['.', '.', '.'],
     ['.', '6', '.'],
     ['8', '.', '.'],
     ['4', '.', '.'],
     ['7', '.', '.'],
     ['.', '6', '.'],
     ['8', '.', '3'],
     ['.', '2', '.'],
     ['.', '.', '3'],
     ['.', '.', '1'],
     ['.', '.', '6'],
     ['.', '6', '.'],
     ['.', '.', '.'],
     ['.', '.', '.'],
     ['.', '.', '.'],
     ['4', '1', '9'],
     ['.', '8', '.'],
     ['2', '8', '.'],
     ['.', '.', '5'],
     ['.', '7', '9']]
     
     with board = (
                [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]])
    
    which goes left to right, then drops one box and repeats itself...
    this was most intuitive to me, but my complex list comprehension;
    boxes = [board[i][col:col+3] for row in [0,3,6] for col in [0,3,6] for i in range(row,row+3)]
    
    lead to a list of 27 lists, so I had to go through them in sets of 3 at a time
    to confirm whether or not there were repeats
    
    '''
    
    for i in range(9):
        hashmap = {}
        for j in range(9):
            if board[i][j] != "." and board[i][j] not in hashmap:
                hashmap[board[i][j]] = 1
            elif board[i][j] != "." and board[i][j] in hashmap:
                return False
            
    for i in range(9):
        hashmap = {}
        for j in range(9):
            if board[j][i] != "." and board[j][i] not in hashmap:
                hashmap[board[j][i]] = 1
            elif board[j][i] != "." and board[j][i] in hashmap:
                return False
    
    boxes = [board[i][col:col+3] for row in [0,3,6] for col in [0,3,6] for i in range(row,row+3)]
    for index in list(range(0, 27, 3)):
        hashmap = {}
        for i in range(index, index + 3):
            array = boxes[i]
            for j in range(3):
                if array[j] != "." and array[j] not in hashmap:
                    hashmap[array[j]] = 1
                elif array[j] != "." and array[j] in hashmap:
                    return False
        
    return True

ans = str(isValidSudoku(board))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect... Correct Answer is " + corr_ans + ", your answer was " + ans)

# Valid Sudoku (using the clever hashmap concept way)

board = (
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

corr_ans = str(True)

def isValidSudoku(board):
    
    '''
    
    with this implementation, we use 9 hashsets for rows, cols and boxes
    to store numbers that are found, and return False if they reoccur
    
    we use box = (row // 3) * 3 + col // 3 to assign box numbers
    rows 0, 1, 2 will essentially be col // 3 due to int divide --> operator \\
    
    '''

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxs = [set() for _ in range(9)]
    
    for row in range(9):
        for col in range(9):
            
            value = board[row][col]
            
            if value == ".":
                continue
                
            if value in rows[row]:
                return False
            rows[row].add(value)
            
            if value in cols[col]:
                return False
            cols[col].add(value)
            
            box = (row // 3) * 3 + col // 3
            if value in boxs[box]:
                return False
            boxs[box].add(value)
    
    return True

ans = str(isValidSudoku(board))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect... Correct Answer is " + corr_ans + ", your answer was " + ans)

# Find Duplicate Subtrees

def findDuplicateSubtrees(root):
        
    '''
    
    idk I took this from editorial, will dissect this later...
    
    '''
    
    from collections import defaultdict
    
    def traverse(node):
        if not node:
            return 0
        triplet = (traverse(node.left), node.val, traverse(node.right))
        if triplet not in triplet_to_id:
            triplet_to_id[triplet] = len(triplet_to_id) + 1
        id = triplet_to_id[triplet]
        cnt[id] += 1
        if cnt[id] == 2:
            res.append(node)
        return id
    triplet_to_id = dict()
    cnt = defaultdict(int)
    res = []
    traverse(root)
    return res

# Jewels and Stones

jewels = "aA"
stones = "aAAbbbb"
corr_ans = str(3)

def numJewelsInStones(jewels, stones):
    
    '''
    
    idk man this one is dumb easy, 
    make a set of chars in jewels
    count how many times a char in jewels appears in stones
    
    '''
    
    hashset = set()
    for s in jewels:
        hashset.add(s)

    ans = 0
    for s in stones:
        if s in hashset:
            ans += 1
            
    return ans

ans = str(isValidSudoku(board))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect... Correct Answer is " + corr_ans + ", your answer was " + ans)

# Longest Substring Without Repeating Characters

s = "abcabcbb"
s = "aab"
s = "dvdf"

def lengthOfLongestSubstring(self, s: str) -> int:
    
    '''
    
    int[26] for Letters 'a' - 'z' or 'A' - 'Z'
    int[128] for ASCII
    int[256] for Extended ASCII
    
    '''
    
    hashset = [None] * 128
    left, right = 0, 0
    ans = 0
    while right < len(s):
        r = s[right]
        index = hashset[ord(r)]
        if index is not None and left <= index < right:
            left = index + 1
        ans = max(ans, right - left + 1)
        hashset[ord(r)] = right
        right += 1
    return ans

# Two Sum III Data Structure

class TwoSum:

    def __init__(self):
        self.TwoSum = []

    def add(self, number: int) -> None:
        self.TwoSum.append(number)

    def find(self, value: int) -> bool:
        
        nums = self.TwoSum
        hashmap = {}
        for i in range(len(nums)):
            complement = value - nums[i]
            if complement in hashmap:
                return True
            hashmap[nums[i]] = i
        return False

twoSum = TwoSum()
print(twoSum.add(1))
print(twoSum.add(3))
print(twoSum.add(5))
print(twoSum.find(4))
print(twoSum.find(7))

# 4Sum II (O(n^2))

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
corr_ans = str(2)

def fourSumCount(nums1, nums2, nums3, nums4):
    
    from collections import defaultdict
    hashmap = defaultdict(int)
    
    for a in nums1:
        for b in nums2:
            hashmap[a + b] += 1

    ans = 0
    for c in nums3:
        for d in nums4:
            if -(c + d) in hashmap:
                ans += hashmap[-(c+d)]
    
    return ans 

ans = str(fourSumCount(nums1, nums2, nums3, nums4))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect... Correct Answer is " + corr_ans + ", your answer was " + ans)

# kSum II (O(n^(k/2)))

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
corr_ans = str(2)

def fourSumCount(nums1, nums2, nums3, nums4):
    
    '''
    
    So this is k-sum, but because I don't want to write a new function 
    for nums5, nums6, nums7... numsk, I just keep it to k = 4. I could've
    opted for just using a list of lists as an input but whatever, I can't 
    test it without leetcode examples anywyay, so i'll keep this in the tank for later
    
    The previous solution involved a hard-coded version for 4Sum II, which 
    involved referencing the list names explicitly in the 1st nested loops, then
    checking if the compliment exists in the 2nd nested loops, and adding 
    the number of combinations found in loop 1, or hashmap[-(c+d)], to ans
    
    The kSum II approach is to generalize this. 
    
    sum_count(lists) will iterate through k//2 lists (if k is odd left list is shorter),
    initialize ans = {0:1} (needed for generalized code, just for the 1st list), get number
    of combinations for nums1, or just the count of each element in the list, then
    re-assign ans to the temp list made at the begininning of each loop. going through
    list a second time will be the equivalent of looping through nums1 then nums2
    like we did for a in nums1 for b in nums2 to build hashmap prior to the compliment code.
    
    This can continue for k//2 loops to gather the total combinations for all sums.
    Last step is to get the total combinations by looping through left hashmaps keys,
    and multiplying the number of combinations of left[key] with right[-key], with
    -ve key being all the compliments found in the right hashmap (defaultdict to avoid key issues).
    If the compliment key isn't in the right hashmap, its left_combinations times 0.
    
    The main benefit for kSum here is reducing the time complexity by a POWER of 2.
    
    
    '''
    
    from collections import defaultdict
    
    def sum_count(lists):
        ans = {0: 1}         # re-assigned in loop, needed for generalized code
        for l in lists:
            temp = defaultdict(int)
            for n in l:
                for total in ans:
                    temp[total + n] += ans[total]
            ans = temp
        return ans

    lists = [nums1, nums2, nums3, nums4]
    k = len(lists)
    left, right = sum_count(lists[:k//2]), sum_count(lists[k//2:])
    return sum(left[s]*right[-s] for s in left)  # combinations come together multiplicitively

ans = str(fourSumCount(nums1, nums2, nums3, nums4))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect... Correct Answer is " + corr_ans + ", your answer was " + ans)

# Top K Frequent Elements

nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
corr_ans = str([1,2])

def topKFrequent(nums, k):
    
    from collections import defaultdict
    hashmap = defaultdict(int)
    
    if k == len(nums):
        return nums
    
    for n in nums:
        hashmap[n] += 1
    
    ans = []
    for i in range(k):
        max_key = 0
        max_count = 0
        for n in hashmap:
            if hashmap[n] > max_count:
                max_key = n
                max_count = hashmap[n]
        ans.append(max_key)
        del hashmap[max_key]
        
    return ans

ans = str(topKFrequent(nums, k))
print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect... Correct Answer is " + corr_ans + ", your answer was " + ans)

# Unique Word Abbreviation

corr_ans = "[null, false, true, false, true, true])"

class ValidWordAbbr:

    '''
    
    Not gonna lie I don't even understand the question so I cheated and looked at the answer (3/5)
    The answer sucks for this editorial so I looked up a good python solution with some
    over the top one liner code which I might translate into more readable multiline code
    
    
    '''
    
    def __init__(self, dictionary):
        from collections import defaultdict
        self.shorten = lambda word: word if len(word) <= 2 else word[0] + str(len(word)-2) + word[-1]
        self.Abbr = defaultdict(set)
        for word in dictionary: self.Abbr[self.shorten(word)].add(word)
        print(self.Abbr)

    def isUnique(self, word: str) -> bool:
        s = self.shorten(word)
        return s not in self.Abbr or word in self.Abbr[s] and len(self.Abbr[s]) == 1
  
str_ans_start = "[null, "
ans = []
validWordAbbr = ValidWordAbbr(["deer", "door", "cake", "card"])
ans.append(validWordAbbr.isUnique("dear")) # return false, dictionary word "deer" and word "dear" have the same abbreviation "d2r" but are not the same.
ans.append(validWordAbbr.isUnique("cart")) # return true, no words in the dictionary have the abbreviation "c2t".
ans.append(validWordAbbr.isUnique("cane")) # return false, dictionary word "cake" and word "cane" have the same abbreviation  "c2e" but are not the same.
ans.append(validWordAbbr.isUnique("make")) # return true, no words in the dictionary have the abbreviation "m2e".
ans.append(validWordAbbr.isUnique("cake")) # return true, because "cake" is already in the dictionary and no other word in the dictionary has "c2e" abbreviation.
ans = str_ans_start + str(ans)

print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect... Correct Answer is " + corr_ans + ", your answer was " + ans)

# Insert Delete GetRandom O(1)

corr_ans = "[null, true, false, true, 2, true, false, 2]"

class RandomizedSet:

    def __init__(self):
        self.randomSet = []

    def insert(self, val):
        if val not in self.randomSet:
            self.randomSet.append(val)
            return True
        return False

    def remove(self, val):
        if val in self.randomSet:
            self.randomSet.remove(val)
            return True
        return False

    def getRandom(self):
        from random import randint
        return self.randomSet[randint(0, len(self.randomSet) - 1)]
    
ans = []
randomizedSet = RandomizedSet()
ans.append(randomizedSet.insert(1)) # Inserts 1 to the set. Returns true as 1 was inserted successfully.
ans.append(randomizedSet.remove(2)) # Returns false as 2 does not exist in the set.
ans.append(randomizedSet.insert(2)) # Inserts 2 to the set, returns true. Set now contains [1,2].
ans.append(randomizedSet.getRandom()) # getRandom() should return either 1 or 2 randomly.
ans.append(randomizedSet.remove(1)) # Removes 1 from the set, returns true. Set now contains [2].
ans.append(randomizedSet.insert(2)) # 2 was already in the set, so return false.
ans.append(randomizedSet.getRandom()) # Since 2 is the only number in the set, getRandom() will always return 2.
ans = str(ans)

print("Correct Solution is: " + corr_ans + " and Algorithm Output Is: " + ans + ". " + "Answers Match!" if corr_ans == ans else "Algorithm is Incorrect... Correct Answer is " + corr_ans + ", your answer was " + ans)
