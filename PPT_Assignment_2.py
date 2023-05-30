"""# Assignment Questions 2

<aside>
💡 **Question 1**
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

**Example 1:**
Input: nums = [1,4,3,2]
Output: 4

**Explanation:** All possible pairings (ignoring the ordering of elements) are:

1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4
</aside>
Algo: 

"""

def question1(j):
    max_sum = 0
    j.sort()
    for i,n in enumerate(j):
        if i%2==0:
            max_sum+=n
    return max_sum
    
nums = [1,4,3,2]
print(question1(nums))


"""
<aside>
💡 **Question 2**
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor. 

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice. 

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

**Example 1:**
Input: candyType = [1,1,2,2,3,3]
Output: 3

**Explanation**: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

</aside>

"""

def question2(i):
    limit = round(len(i)/2)
    cont = 0
    o = []
    for n in i:
        if n not in o:
            o.append(n)
    if len(o) > limit:
        return limit
    else:
        return len(o)
            
    
i=[1,1,2,2,3,3,4,5,6,7]
print(question2(i))


"""
<aside>
💡 **Question 3**
We define a harmonious array as an array where the difference between its maximum value
and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence
among all its possible subsequences.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

**Example 1:**
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5

**Explanation:** The longest harmonious subsequence is [3,2,2,2,3].

</aside>
"""
def question3( nums):
         d, a = {}, 0
        for i in nums:
            if i not in d: d[i] = 1
            else: d[i] += 1
        for i in d:
            if i + 1 in d.keys():
                a = max(a, d[i] + d[i+1])
        print(d)        
        return a
i= [1,3,2,2,5,2,3,77,77,77,77,77,77,78,78]
print(question3(i))
"""
<aside>
💡 **Question 4**
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

**Example 1:**
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

</aside>
"""
def question4(j,n):
            if n ==0:
                return True
            else:
                for i in range(len(j)):
                    if j[i] == 0 and (i == 0 or j[i-1] == 0) and (i == len(j)-1 or j[i+1] == 0):
                            j[i] = 1
                            n -= 1
                            if n == 0:
                             return True
                return False
nums = [1,0,0,0,1]
n = 1
print(question4(nums,n))


"""
<aside>
💡 **Question 5**
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

**Example 1:**
Input: nums = [1,2,3]
Output: 6

</aside>
"""
def question5(j):
     if len(j) == 3:
         return j[0] * j[1] * j[2]
     else:
         max1 = max2 = max3 = -1000 
         min1 = min2 = 1000
         for i in j:
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:
                max3 = i
            if i < min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min2 = i
         return max(max1 * max2 * max3, min1 * min2 * max1)
nums = [1,-4,-3,-2]
print(question5(nums))
"""
<aside>
💡 **Question 6**
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise,
return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

**Explanation:** 9 exists in nums and its index is 4

</aside>
"""
def question6(i,k):
    for n in range(0,len(i)):
        if i[n]==k:
            return n
        else:
            return -1
nums = [-1,0,3,5,9,12]
target = 10
print(question6(nums,target))
"""
<aside>
💡 **Question 7**
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

**Example 1:**
Input: nums = [1,2,2,3]
Output: true

</aside>
"""
def question7(i):
    mi = 1
    md = 1
    for n in range(0,len(i)-1):
        if i[n]<= i[n+1]:
            mi=mi+1
    for m in range (0,len(i)-1):
        if i[m]>= i[m+1]:
            md=md+1
    print(md)
    print(mi)
    print(len(i))
    if md== len(i) or mi == len(i):
        return True
    else:
        return False
nums  = [1,2,2,3,9,4]
print(question7(nums))

"""
<aside>
💡 **Question 8**
You are given an integer array nums and an integer k.

In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.

The score of nums is the difference between the maximum and minimum elements in nums.

Return the minimum score of nums after applying the mentioned operation at most once for each index in it.

**Example 1:**
Input: nums = [1], k = 0
Output: 0

**Explanation:** The score is max(nums) - min(nums) = 1 - 1 = 0.

</aside>
"""

def question8(nums, k):
        x=max(nums)
        y=min(nums)
        return max(0,(x-k)-(y+k))
nums = [0,10]
k = 2
print(question8(nums,k))