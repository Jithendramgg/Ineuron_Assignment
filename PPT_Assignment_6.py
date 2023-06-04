# Assignment Questions 6

"""
💡 **Question 1**

A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

- s[i] == 'I' if perm[i] < perm[i + 1], and
- s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return **any of them**.

**Example 1:**

**Input:** s = "IDID"

**Output:**

[0,4,1,3,2]

"""
def q1(a):
    L,i,l=[],0,len(a)
    for k in a:
        if k=='I':
            L.append(i)
            i+=1
        else:
            L.append(l)
            l-=1
    if a[-1]=='I':
        L.append(i)
    else: L.append(l)
    return L
a = 'IDID'
print(q1(a))
"""
💡 **Question 2**

You are given an m x n integer matrix matrix with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true *if* target *is in* matrix *or* false *otherwise*.

You must write a solution in O(log(m * n)) time complexity.

**Example 1:**

![Screenshot 2023-05-29 005303.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e4b0271f-15f0-4744-826b-18500ccfcb75/Screenshot_2023-05-29_005303.png)



**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

**Output:** true

"""
def q2(a,t):
    for i in a:
        if t in i:
            return True
            break
        else: return False
a = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
t = 99
print(q2(a,t))
"""
💡 **Question 3**

Given an array of integers arr, return *true if and only if it is a valid mountain array*.

Recall that arr is a mountain array if and only if:

- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
    - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

![Screenshot 2023-05-29 005352.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5565e778-ac57-4ced-85a2-ccb13268bdf6/Screenshot_2023-05-29_005352.png)



**Example 1:**

**Input:** arr = [2,1]

**Output:**

false

"""
def q3(a):
    m = max(a)
    print(m)
    p,inc=0,1
    if len(a)<3:
        return False
    elif len(a)==3:
        if a[1]<a[0] or a[1] < a[2]:
            return False
    else:
        for i in range(len(a)-1):
            if a[i]< a[i+1] and p==0:
                if a[i+1]==m:
                  p=1
                inc=inc+1
            elif a[i]>a[i+1] and p==1:
                 inc=inc+1
        if inc == len(a):
            return True
        else: return False
            
            
a= [1,3,4,5]
print(q3(a))
"""
💡 **Question 4**

Given a binary array nums, return *the maximum length of a contiguous subarray with an equal number of* 0 *and* 1.

**Example 1:**

**Input:** nums = [0,1]

**Output:** 2

**Explanation:**

[0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

"""
def q4(n):
    m=0
    c=0
    d={0:-1}
    for i in range(len(n)):
        c+=1 if n[i]==1 else -1
        if c in d:
            m=max(m,i-d[c])
        else:
            d[c]=i
    return m
n = [0,1,1,0]
print(q4(n))
"""
💡 **Question 5**

The **product sum** of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (**0-indexed**).

- For example, if a = [1,2,3,4] and b = [5,2,3,1], the **product sum** would be 1*5 + 2*2 + 3*3 + 4*1 = 22.

Given two arrays nums1 and nums2 of length n, return *the **minimum product sum** if you are allowed to **rearrange** the **order** of the elements in* nums1.

**Example 1:**

**Input:** nums1 = [5,3,4,2], nums2 = [4,2,2,5]

**Output:** 40

**Explanation:**

We can rearrange nums1 to become [3,5,4,2]. The product sum of [3,5,4,2] and [4,2,2,5] is 3*4 + 5*2 + 4*2 + 2*5 = 40.

"""
def q5(n,m):
    o=0
    n.sort()
    m.sort(reverse=True)
    print(n,m)
    for i in range(len(n)):
        o+=n[i]*m[i]
    return o
n = [5,3,4,2]
m = [4,2,2,5]
print(q5(n,m))
"""
💡 **Question 6**

An integer array original is transformed into a **doubled** array changed by appending **twice the value** of every element in original, and then randomly **shuffling** the resulting array.

Given an array changed, return original *if* changed *is a **doubled** array. If* changed *is not a **doubled** array, return an empty array. The elements in* original *may be returned in **any** order*.

**Example 1:**

**Input:** changed = [1,3,4,2,6,8]

**Output:** [1,3,4]

**Explanation:** One possible original array could be [1,3,4]:

- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.

Other original arrays could be [4,3,1] or [3,1,4].

"""
def q6(nums):
    o=[]
    for i in range(len(nums)//2):
        for j in range(i+1,len(nums)):
            #print(i,j)
            if nums[i]*2==nums[j]:
                #print(i,j)
                o.append(nums[i])
    return o
nums=[1,3,4,2,6,8]
print(q6(nums))


"""
💡 **Question 7**

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

**Example 1:**

**Input:** n = 3

**Output:** [[1,2,3],[8,9,4],[7,6,5]]

"""
def q7(n):
    mat=[[0]*n for _ in range(n) ]
    #return mat
    num,left,right,top,bottom=1,0,n-1,0,n-1
    while num<=n*n:
        for i in range(left,right+1):
            mat[top][i]= num
            num+=1
        top+=1
        for i in range(top,bottom+1):
            mat[i][right]=num
            num+=1
        right-=1
        for i in range(right,left-1,-1):
            mat[bottom][i]=num
            num+=1
        bottom-=1
        for i in range(bottom,top-1,-1):
            mat[i][left]=num
            num+=1
        left+=1    
    return mat
n=3
print(q7(n))
"""
💡 **Question 8**

Given two [sparse matrices] mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

**Example 1:**



**Input:** mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]

**Output:**

[[7,0,0],[-7,0,3]]

"""
def q8(n,m):
    n1,n2=len(n),len(n[0])
    m1,m2=len(m),len(m[0])
    out= [[0]*m2 for _ in range(n1)]
    for i in range(n1):
        for j in range(m2):
            for x in range(m1):
                out[i][j] += n[i][x] * m[x][j]
    return out
n = [[1,0,0],[-1,0,3]]
m = [[7,0,0],[0,0,0],[0,0,1]]
print(q8(n,m))