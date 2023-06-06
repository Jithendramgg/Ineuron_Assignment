# Assignment Questions 7

"""
💡 **Question 1**

Given two strings s and t, *determine if they are isomorphic*.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**

**Input:** s = "egg", t = "add"

**Output:** true

"""
def q1(s,t):
    cm={}
    if len(s)!=len(t):
        return False
    else:
        for i in range(len(s)):
            if s[i] in :
                if t[i]!=cm[s[i]]:
                    return False
            else:
                cm[s[i]]=t[i]
        return True
    
s='egg'
t='djh'
print(q1(s,t))

"""
💡 **Question 2**

Given a string num which represents an integer, return true *if* num *is a **strobogrammatic number***.

A **strobogrammatic number** is a number that looks the same when rotated 180 degrees (looked at upside down).

**Example 1:**

**Input:** num = "69"

**Output:**

true

"""
def q2(n):
    m = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    l,r=0,len(n)-1
    while l<=r:
        if n[l] not in m or n[l] != m[n[r]]:
            return False
        l+=1
        r-=1
    return True

n='886'    
print(q2(n))
"""
💡 **Question 3**

Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

**Example 1:**

**Input:** num1 = "11", num2 = "123"

**Output:**

"134"

"""
def q3(n,m):
    c=0
    i=len(n)-1
    j=len(m)-1
    r=''
    cur_sum=0
    while i>=0 or j>=0 or c>0:
        d1= int(n[i]) if i>=0 else 0
        d2 =int(m[j]) if j>=0 else 0
        cur_sum = d1+d2+c
        c=cur_sum//10
        r=str(cur_sum%10)+r
        i-=1
        j-=1
    return r

n='886' 
m='11'
print(q3(n,m))

"""
💡 **Question 4**

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

**Example 1:**

**Input:** s = "Let's take LeetCode contest"

**Output:** "s'teL ekat edoCteeL tsetnoc"

"""
def q4(s):
    c=s.split(' ')
    s=''
    for i in c:
        s=s+(i[::-1])+' '
    return s

s='this is python'
print(q4(s))
"""
💡 **Question 5**

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

**Example 1:**

**Input:** s = "abcdefg", k = 2

**Output:**

"bacdfeg"

"""
def q5(n,k):
    s=list(n)
    l=len(s)
    r=''
    for i in range(0,l,2*k):
        left=i
        right=min(i+k-1,l-1)
        while(left<=right):
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
    print(s)
    r="".join(s)    
    
n='8863456321345' 
k=2
print(q5(n,k))
"""
💡 **Question 6**

Given two strings s and goal, return true *if and only if* s *can become* goal *after some number of **shifts** on* s.

A **shift** on s consists of moving the leftmost character of s to the rightmost position.

- For example, if s = "abcde", then it will be "bcdea" after one shift.

**Example 1:**

**Input:** s = "abcde", goal = "cdeab"

**Output:**

true

"""
def q6(n,k):
    if len(n)!=len(k):
     return False
    if n==k:
        return True
    for _ in range(len(n)):
        n=n[1:]+n[0]
        if n==k:
            return True
    return False
n='abcde' 
k='bceda'
print(q6(n,k))
"""
💡 **Question 7**

Given two strings s and t, return true *if they are equal when both are typed into empty text editors*. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

**Example 1:**

**Input:** s = "ab#c", t = "ad#c"

**Output:** true

**Explanation:**

Both s and t become "ac".

"""
def q7(n,k):
    def q7_1(s):
        o=[]
        for i in s:
            if i=='#':
                o.pop()
            elif i != '#':
                o.append(i)
        return o
    return q7_1(n)== q7_1(k)
        
        
n='ab#de' 
k='ac#de'
print(q7(n,k))
"""
💡 **Question 8**

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

**Example 1:**

![Screenshot 2023-05-29 010117.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/012b0a97-4e4b-49b6-bc95-0531fc712978/Screenshot_2023-05-29_010117.png)

**Input:** coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

**Output:** true

"""
def q8(n):
    def slope(p1,p2):
     x1,y1,x2,y2=p1[0],p1[1],p2[0],p2[1]
     if x2 - x1 == 0:
            return float('inf')
     else:
        s=(y2-y1)/(x2-x1)
     return s
    ref_s = slope(n[0],n[1])
    for i in range(1,len(n)-1):
        cur_s = slope(n[i],n[i+1])
        if cur_s!=ref_s:
            return False
    return True

n=[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(q8(n))