# Assignment Questions 8

"""
💡 **Question 1**

Given two strings s1 and s2, return *the lowest **ASCII** sum of deleted characters to make two strings equal*.

**Example 1:**

**Input:** s1 = "sea", s2 = "eat"

**Output:** 231

**Explanation:** Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.

Deleting "t" from "eat" adds 116 to the sum.

At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

"""
def q1(s1, s2):
    memo = {}  # Memoization dictionary to store computed results
    
    # Recursive function to calculate the minimum ASCII sum
    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Base cases
        if i == len(s1):
            result = sum(ord(ch) for ch in s2[j:])
        elif j == len(s2):
            result = sum(ord(ch) for ch in s1[i:])
        elif s1[i] == s2[j]:
            result = helper(i+1, j+1)
        else:
            delete_s1 = ord(s1[i]) + helper(i+1, j)
            delete_s2 = ord(s2[j]) + helper(i, j+1)
            result = min(delete_s1, delete_s2)
        
        memo[(i, j)] = result
        return result
    
    return helper(0, 0)
s1='eat'
s2='sea'
print(q1(s1,s2))

"""
💡 **Question 2**

Given a string s containing only three types of characters: '(', ')' and '*', return true *if* s *is **valid***.

The following rules define a **valid** string:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

**Example 1:**

**Input:** s = "()"

**Output:**

true

"""
def q2(s):
    stack = []
    asterisk_stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == '*':
            asterisk_stack.append(len(stack))
        elif char == ')':
            if stack:
                stack.pop()
            elif asterisk_stack:
                asterisk_stack.pop()
            else:
                return False
    
    while stack and asterisk_stack:
        if stack[-1] > asterisk_stack[-1]:
            return False
        stack.pop()
        asterisk_stack.pop()
    
    return len(stack) == 0

s='())'
print(q2(s))

"""
💡 **Question 3**

Given two strings word1 and word2, return *the minimum number of **steps** required to make* word1 *and* word2 *the same*.

In one **step**, you can delete exactly one character in either string.

**Example 1:**

**Input:** word1 = "sea", word2 = "eat"

**Output:** 2

**Explanation:** You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

"""
def q3(s1, s2):
    m, n = len(s1), len(s2)
    
    # Create a 2D table to store the lengths of LCS
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Fill the table bottom-up
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    lcs_length = dp[m][n]
    steps = (m - lcs_length) + (n - lcs_length)
    
    return steps

s1='eat'
s2='sea'
print(q3(s1,s2))

"""
💡 **Question 4**

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
You always start to construct the **left** child node of the parent first if it exists.

![Screenshot 2023-05-29 010548.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bdbea2d1-34a4-4c4b-a450-ea6db7410c43/Screenshot_2023-05-29_010548.png)

**Input:** s = "4(2(3)(1))(6(5))"

**Output:** [4,2,6,3,1,5]

"""
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def str2tree(s):
    if not s:
        return None

    stack = []
    i = 0

    while i < len(s):
        if s[i].isdigit() or s[i] == '-':
            # Extract the number and create a new node
            j = i + 1
            while j < len(s) and (s[j].isdigit() or s[j] == '-'):
                j += 1
            value = int(s[i:j])
            node = TreeNode(value)
            stack.append(node)
            i = j
        elif s[i] == '(':
            # Move to the left child
            i += 1
        elif s[i] == ')':
            # Finished constructing left subtree, move to right child
            parent = stack.pop()
            if stack:
                if not stack[-1].left:
                    stack[-1].left = parent
                else:
                    stack[-1].right = parent
            i += 1

    return stack[0] if stack else None


"""
💡 **Question 5**

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of **consecutive repeating characters** in chars:

- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string s **should not be returned separately**, but instead, be stored **in the input character array chars**. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done **modifying the input array,** return *the new length of the array*.

You must write an algorithm that uses only constant extra space.

**Example 1:**

**Input:** chars = ["a","a","b","b","c","c","c"]

**Output:** Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

**Explanation:**

The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

"""
def q5(s):
    read = write = 0
    count = 1
    
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            s[write] = s[read]
            write += 1
            if count > 1:
                count_str = str(count)
                for j in range(len(count_str)):
                    s[write] = count_str[j]
                    write += 1
            count = 1
            read = i
    
    return write
s=["a","a","b","b","c","c","c"]
print(q5(s))

"""
💡 **Question 6**

Given two strings s and p, return *an array of all the start indices of* p*'s anagrams in* s. You may return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

**Input:** s = "cbaebabacd", p = "abc"

**Output:** [0,6]

**Explanation:**

The substring with start index = 0 is "cba", which is an anagram of "abc".

The substring with start index = 6 is "bac", which is an anagram of "abc".

"""
from collections import Counter

def q6(s, p):
    result = []
    p_count = Counter(p)
    s_count = Counter(s[:len(p)])  # Initialize the frequency counter for the first window
    
    if s_count == p_count:
        result.append(0)
    
    for i in range(1, len(s) - len(p) + 1):
        # Update the frequency counter by adding the new character and removing the leftmost character
        s_count[s[i-1]] -= 1
        if s_count[s[i-1]] == 0:
            del s_count[s[i-1]]
        s_count[s[i+len(p)-1]] += 1
        
        if s_count == p_count:
            result.append(i)
    
    return result
s = "cbaebabacd"
p = "abc"
print(q6(s,p))

"""
💡 **Question 7**

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

**Example 1:**

**Input:** s = "3[a]2[bc]"

**Output:** "aaabcbc"

"""
def q7(s):
    stack = []
    current_string = ""
    current_count = 0

    for char in s:
        if char.isdigit():
            current_count = current_count * 10 + int(char)
        elif char == "[":
            stack.append(current_count)
            stack.append(current_string)
            current_count = 0
            current_string = ""
        elif char == "]":
            prev_string = stack.pop()
            repetition_count = stack.pop()
            current_string = prev_string + current_string * repetition_count
        else:
            current_string += char

    return current_string
    
s = "3[a]2[bc]"
print(q7(s))
"""
💡 **Question 8**

Given two strings s and goal, return true *if you can swap two letters in* s *so the result is equal to* goal*, otherwise, return* false*.*

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

- For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

**Example 1:**

**Input:** s = "ab", goal = "ba"

**Output:** true

**Explanation:** You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

"""
def q8(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:
        # Check if there are at least two identical characters in s
        seen = set()
        for char in s:
            if char in seen:
                return True
            seen.add(char)
        return False

    indices = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            indices.append(i)
        if len(indices) > 2:
            return False

    if len(indices) != 2:
        return False

    i, j = indices[0], indices[1]
    return s[i] == goal[j] and s[j] == goal[i]
s = "ab"
goal = "ba"
print(q8(s,goal))