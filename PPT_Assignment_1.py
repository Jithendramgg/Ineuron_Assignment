""" <aside>
💡 **Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example:**
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1][

</aside>"""

def ass_que_1(i, j):
    for n in range(0,len(i)):
     for m in range(n,len(i)):
        if i[n] + i[m] == j:
            o = [n,m]
            break
    return o
# driver program
i = [2,3,4,5,1]
j = 9
print(ass_que_1(i,j))

#Ans :[2, 3]

""" <aside>
💡 **Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

**Example :**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_*,_*]

**Explanation:** Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores)[

</aside>"""

def ass_que_1(i, j):
    k = len(i)
    o=[]
    print(type(k))
    print("sort" ,i)
    ji= i.count(j)
    for pr in range (0,ji):
        i.remove(j)
    return len(i)
# driver program
i = [2,3,4,5,14,4,4]
j = 3
print(ass_que_1(i,j))


"""
<aside>
💡 **Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5

Output: 2

</aside>
"""

def ass_que_3(i, j):
    if i[len(i)-1]< j:
        return len(i)
    elif j<= i[len(i)-1]:
     for n in range(0,len(i)-1):
        print("index",n)
        print("val",i[n])
        if i[n]==j:
            return n
        elif i[n]<j and i[n+1]> j:
            return n+1
# driver program
i = [2,3,6,8]
j = 7  #4
print(ass_que_3(i,j))

"""<aside>
💡 **Q4.** You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

**Explanation:** The array represents the integer 123.

Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

</aside>"""

def ass_que_4(v):
    p = len(v)-1
    val =0
    out = []
    for n in v:
        val = val+ n* (10**p)
        p=p-1
    val=val+1
    for n in range(0,len(str(val))):
        out.append(int(str(val)[n]))
    return out

# driver program
v =  [9,9,9]
print(ass_que_4(v))

""" 
<aside>
💡 **Q5.** You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

**Example 1:**
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

**Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1

</aside>
"""
def merge( nums1, m, nums2, n):
         i , j = m-1 , n-1
         counter = (m+n)-1
         while j >= 0  and i >= 0:
            print("inside while start",j,i,counter,nums1,nums2)
            if nums2[j] >= nums1[i]: 
                nums1[counter] = nums2[j]
                counter -= 1
                j -= 1
                print("inside if start",j,i,counter,nums1,nums2)
            else:
                nums1[counter] = nums1[i]
                nums1[i] = 0
                counter -= 1
                i -=1
                print("inside else start",j,i,counter,nums1,nums2)
        
         if j >= 0:
            for k in range(j+1):
                nums1[k] = nums2[k]
                print("inside k start",j,i,counter,nums1,nums2)
         print(nums1)
         
#or#
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
for n in range(0,len(nums2)):
    nums1.append(nums2[n])
    nums1.sort()
    nums1.remove(0)
            
print(nums1)
"""
<aside>
💡 **Q6.** Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]

Output: true

</aside>
"""
def ass_que_6(i):
    i.sort()
    o="False"
    for n in range(0,len(i)-1):
        if i[n]==i[n+1]:
            o="True"
    return o   
# driver program
i =  [1,2,3]
print(ass_que_6(i))

"""<aside>
💡 **Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

</aside>"""

def ass_que_7(i):
    i.sort()
    for n in i:
        if n == 0:
            i.append(0)
            i.remove(n)
    return i    
# driver program
i =  [0,1,0,3,0,12]
print(ass_que_7(i))


"""<aside>
💡 **Q8.** You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

**Example 1:**
Input: nums = [1,2,2,4]
Output: [2,3]

</aside>"""

def ass_que_8(i):
    for n in range(0,len(i)-1):
        if i[n]==i[n+1]:
            return [i[n],i[n]+1]
        
# driver program
i = [1,2,3,4,5,6,7,8,8]
print(ass_que_8(i))
