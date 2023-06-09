# Assignment Questions 9

"""
💡 **Question 1**

Given an integer `n`, return *`true` if it is a power of two. Otherwise, return `false`*.

An integer `n` is a power of two, if there exists an integer `x` such that `n == 2x`.

**Example 1:**
Input: n = 1 

Output: true

**Example 2:**
Input: n = 16 

Output: true

**Example 3:**
Input: n = 3 

Output: false

"""
def q1(n):
    if n==1:
        return True
    elif (n)%2!=0:
        return False
    else:
        return q1(n//2)
n=16
print(q1(n))


"""
💡 **Question 2**

Given a number n, find the sum of the first natural numbers.

**Example 1:**

Input: n = 3 

Output: 6

**Example 2:**

Input  : 5 

Output : 15

"""
def q2(n):
    if n==1:
        return 1
    else:
        return n+q2(n-1)
n=5
print(q2(n))


"""
💡 **Question 3**

****Given a positive integer, N. Find the factorial of N. 

**Example 1:**

Input: N = 5 

Output: 120

**Example 2:**

Input: N = 4

Output: 24

"""
def q3(n):
    if n==1:
        return 1
    else:
        return n*q3(n-1)
n=5
print(q3(n))


"""
💡 **Question 4**

Given a number N and a power P, the task is to find the exponent of this number raised to the given power, i.e. N^P.

**Example 1 :** 

Input: N = 5, P = 2

Output: 25

**Example 2 :**
Input: N = 2, P = 5

Output: 32

"""
def q4(n,p):
    if p==0:
        return 1
    else:
        return n*q4(n,p-1)
n=5
p=2
print(q4(n,p))


"""
💡 **Question 5**

Given an array of integers **arr**, the task is to find maximum element of that array using recursion.

**Example 1:**

Input: arr = {1, 4, 3, -5, -4, 8, 6};
Output: 8

**Example 2:**

Input: arr = {1, 4, 45, 6, 10, -8};
Output: 45

"""
def findMax(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], findMax(arr[1:]))

arr = [1, 4, 3, -5, -4, 8, 6]
max_element = findMax(arr)
print(max_element)  # Output: 8

"""
💡 **Question 6**

Given first term (a), common difference (d) and a integer N of the Arithmetic Progression series, the task is to find Nth term of the series.

**Example 1:**

Input : a = 2 d = 1 N = 5
Output : 6
The 5th term of the series is : 6

**Example 2:**

Input : a = 5 d = 2 N = 10
Output : 23
The 10th term of the series is : 23

"""
def q6(a, d, n):
    if n == 1:
        return a
    else:
        return q6(a, d, n - 1) + d
a=2
d=1
n=5
print(q6(a,d,n))
"""
💡 **Question 7**

Given a string S, the task is to write a program to print all permutations of a given string.

**Example 1:**

***Input:***

*S = “ABC”*

***Output:***

*“ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”*

**Example 2:**

***Input:***

*S = “XY”*

***Output:***

*“XY”, “YX”*

"""
def permutations(S, left, right):
    if left == right:
        print("".join(S))
    else:
        for i in range(left, right + 1):
            S[left], S[i] = S[i], S[left]
            permutations(S, left + 1, right)
            S[left], S[i] = S[i], S[left]  # backtrack

# Wrapper function to initiate the recursion
def printPermutations(S):
    permutations(list(S), 0, len(S) - 1)

S = 'XYZ'
printPermutations(S)

"""
💡 **Question 8**

Given an array, find a product of all array elements.

**Example 1:**

Input  : arr[] = {1, 2, 3, 4, 5}
Output : 120
**Example 2:**

Input  : arr[] = {1, 6, 3}
Output : 18

"""
def q8(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * q8(arr[1:])

# Example usage
arr1 = [1, 2, 3, 4, 5]
print(q8(arr1))  # Output: 120
