"""# Assignment Questions 4

<aside>
💡 **Question 1**
Given three integer arrays arr1, arr2 and arr3 **sorted** in **strictly increasing** order, return a sorted array of **only** the integers that appeared in **all** three arrays.

**Example 1:**

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]

Output: [1,5]

**Explanation:** Only 1 and 5 appeared in the three arrays.

</aside>

<aside>
"""
def q1 (a1,a2,a3):
    o=[]
    for i in a1:
        for j in a2:
            for k in a3:
                #print(i,j,k)
                if i==j==k:
                    o.append(i)
                    continue 
    print(o)               
a1 = [1,2,3,4,5]
a2 = [1,2,5,7,9]
a3 = [1,3,4,5,8]
print(q1(a1,a2,a3))

"""
💡 **Question 2**

Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*

- answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
- answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.

**Note** that the integers in the lists may be returned in **any** order.

**Example 1:**

**Input:** nums1 = [1,2,3], nums2 = [2,4,6]

**Output:** [[1,3],[4,6]]

**Explanation:**

For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].

For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

</aside>

<aside>
"""
def q2(nums1, nums2):
        n1=set(nums1)
        n2=set(nums2)
        r1=list(set(x for x in nums1 if x not in n2))
        r2=list(set(x for x in nums2 if x not in n1))
        return [r1,r2]
nums1 = [1,2,3]
nums2 = [2,4,6]
print(q2(nums1,nums2))


"""
💡 **Question 3**
Given a 2D integer array matrix, return *the **transpose** of* matrix.

The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

**Example 1:**

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [[1,4,7],[2,5,8],[3,6,9]]

![iamge_v3.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a54805f4-c9b5-491c-a900-8e8a94062c79/iamge_v3.png)

</aside>

<aside>
"""
def q3(a):
    o=[[],[],[]]
    i,j,k=0,0,0
    while (k<9):
        o[j].append(a[i][j])
        if i<2:
            i=i+1
        elif i==2:    
            i,j=0,j+1
        
        k=k+1
    print(o)
    
a=[[1,2,3],[4,5,6],[7,8,9]]
print(q3(a))
"""
💡 **Question 4**
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is **maximized**. Return *the maximized sum*.

**Example 1:**

Input: nums = [1,4,3,2]

Output: 4

**Explanation:** All possible pairings (ignoring the ordering of elements) are:

1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3

2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3

3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4

So the maximum possible sum is 4.

</aside>

<aside>
"""
def question4(j):
    max_sum = 0
    j.sort()
    for i,n in enumerate(j):
        if i%2==0:
            max_sum+=n
    return max_sum
    
nums = [1,4,3,2]
print(question4(nums))

"""
💡 **Question 5**
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.

Given the integer n, return *the number of **complete rows** of the staircase you will build*.

**Example 1:**

[]()

![v2.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4bd91cfa-d2b1-47b3-8197-a72e8dcfff4b/v2.jpg)

**Input:** n = 5

**Output:** 2

**Explanation:** Because the 3rd row is incomplete, we return 2.

</aside>

<aside>
"""
import math
def q5(n):
        return int(math.sqrt(2 * n + 0.25) - 0.50)
n=5
print(q5(n))
"""
💡 **Question 6**
Given an integer array nums sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

**Example 1:**

Input: nums = [-4,-1,0,3,10]

Output: [0,1,9,16,100]

**Explanation:** After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]

</aside>

<aside>
"""
def q6(a):
    o=[]
    for i in a:
        o.append(i*i)
    #print(o)
    o.sort()
    print(o)
   
a=[4,-1,0,3,10] 
print(q6(a))
"""
💡 **Question 7**
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return *the number of maximum integers in the matrix after performing all the operations*

**Example 1:**

![q4.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4d0890d0-7bc7-4f59-be8e-352d9f3c1c52/q4.jpg)

**Input:** m = 3, n = 3, ops = [[2,2],[3,3]]

**Output:** 4

**Explanation:** The maximum integer in M is 2, and there are four of it in M. So return 4.

</aside>

<aside>
"""
def q7(m, n, ops):
        length = len(ops)
        if length == 0:
            return m*n
        result = [ops[0][0] , ops[0][1]]
        for i in range(1,length):
            result[0] = min(result[0] , ops[i][0])
            result[1] = min(result[1] , ops[i][1])
        return result[0]*result[1] 
m = 3
n = 3
ops = [[2,2],[3,3]]
print(q7(m,n,ops))    
"""
💡 **Question 8**

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

*Return the array in the form* [x1,y1,x2,y2,...,xn,yn].

**Example 1:**

**Input:** nums = [2,5,1,3,4,7], n = 3

**Output:** [2,3,5,4,1,7]

**Explanation:** Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

</aside>
"""
def q8(a,n):
    o=[]
    for i in range(n):
        print(i)
        o.append(a[i])
        o.append(a[i+n])
    print(o)
a=[2,5,1,3,4,7]
n=3
print(q8(a,n))