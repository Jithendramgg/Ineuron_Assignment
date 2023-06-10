# Assignment Questions 10

"""
💡 **Question 1**

Given an integer `n`, return *`true` if it is a power of three. Otherwise, return `false`*.

An integer `n` is a power of three, if there exists an integer `x` such that `n == 3x`.

**Example 1:**


Input: n = 27
Output: true
Explanation: 27 = 33

def q1(n):
    if n==1:
        return True
    elif n%3!=0 or n<=0:
        return False
    else:
        return q1(n/3)
n=6
print(q1(n))
    
**Example 2:**

```
Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

```

**Example 3:**

```
Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
```

"""
def q1(n):
    if n==1:
        return True
    elif n%3!=0 or n<=0:
        return False
    else:
        return q1(n/3)
n=6
print(q1(n))
    
"""
💡 **Question 2**

You have a list `arr` of all integers in the range `[1, n]` sorted in a strictly increasing order. Apply the following algorithm on `arr`:

- Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
- Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
- Keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Given the integer `n`, return *the last number that remains in* `arr`.

**Example 1:**

```
Input: n = 9
Output: 6
Explanation:
arr = [1, 2,3, 4,5, 6,7, 8,9]
arr = [2,4, 6,8]
arr = [2, 6]
arr = [6]

```

**Example 2:**

```
Input: n = 1
Output: 1
```

"""
def last_remaining_number(n):
    # Helper function to simulate the algorithm recursively
    def helper(start, end, step):
        if start == end:
            return start

        if step > 0:
            return helper(start + 2 * step, end, -step)
        else:
            if (end - start) % abs(step) == 0:
                return helper(start, end - abs(step), -step)
            else:
                return helper(start, end - abs(step), -step) + step

    return helper(1, n, 1)

# Test the function
n = int(input("Enter the value of n: "))
result = last_remaining_number(n)
print("Last number that remains:", result)


"""
💡 **Question 3**

****Given a set represented as a string, write a recursive code to print all subsets of it. The subsets can be printed in any order.

**Example 1:**

Input :  set = “abc”

Output : { “”, “a”, “b”, “c”, “ab”, “ac”, “bc”, “abc”}

**Example 2:**

Input : set = “abcd”

Output : { “”, “a” ,”ab” ,”abc” ,”abcd”, “abd” ,”ac” ,”acd”, “ad” ,”b”, “bc” ,”bcd” ,”bd” ,”c” ,”cd” ,”d” }

"""
def print_subsets(remaining_set, current_subset):
    if len(remaining_set) == 0:
        print(current_subset)
        return

    # Include the first element of the remaining set
    print_subsets(remaining_set[1:], current_subset + remaining_set[0])

    # Exclude the first element of the remaining set
    print_subsets(remaining_set[1:], current_subset)

# Test the function
set_string = input("Enter the set as a string (e.g., '123'): ")
print("Subsets of the set:")
print_subsets(set_string, "")

"""
💡 **Question 4**

Given a string calculate length of the string using recursion.

**Examples:**

```
Input : str = "abcd"
Output :4

Input : str = "GEEKSFORGEEKS"
Output :13
```

"""
def calculate_length(string):
    if string == "":
        return 0
    else:
        return 1 + calculate_length(string[1:])

# Test the function
string = input("Enter a string: ")
length = calculate_length(string)
print("Length of the string:", length)

"""
💡 **Question 5**

We are given a string S, we need to find count of all contiguous substrings starting and ending with same character.

**Examples :**

```
Input  : S = "abcab"
Output : 7
There are 15 substrings of "abcab"
a, ab, abc, abca, abcab, b, bc, bca
bcab, c, ca, cab, a, ab, b
Out of the above substrings, there
are 7 substrings : a, abca, b, bcab,
c, a and b.

Input  : S = "aba"
Output : 4
The substrings are a, b, a and aba
```

"""
def count_substrings(S):
    count = 0
    n = len(S)

    # Iterate over each character in the string
    for i in range(n):
        # Count substrings ending at index i
        for j in range(i, n):
            # Check if the substring starts and ends with the same character
            if S[i] == S[j]:
                count += 1

    return count

# Test the function
string = input("Enter a string: ")
result = count_substrings(string)
print("Count of contiguous substrings:", result)


"""
💡 **Question 6**

The [tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) is a famous puzzle where we have three rods and **N** disks. The objective of the puzzle is to move the entire stack to another rod. You are given the number of discs **N**. Initially, these discs are in the rod 1. You need to print all the steps of discs movement so that all the discs reach the 3rd rod. Also, you need to find the total moves.**Note:** The discs are arranged such that the **top disc is numbered 1** and the **bottom-most disc is numbered N**. Also, all the discs have **different sizes** and a bigger disc **cannot** be put on the top of a smaller disc. Refer the provided link to get a better clarity about the puzzle.

**Example 1:**

```
Input:
N = 2
Output:
move disk 1 from rod 1 to rod 2
move disk 2 from rod 1 to rod 3
move disk 1 from rod 2 to rod 3
3
Explanation:For N=2 , steps will be
as follows in the example and total
3 steps will be taken.
```

**Example 2:**

```
Input:
N = 3
Output:
move disk 1 from rod 1 to rod 3
move disk 2 from rod 1 to rod 2
move disk 1 from rod 3 to rod 2
move disk 3 from rod 1 to rod 3
move disk 1 from rod 2 to rod 1
move disk 2 from rod 2 to rod 3
move disk 1 from rod 1 to rod 3
7
Explanation:For N=3 , steps will be
as follows in the example and total
7 steps will be taken.
```

"""
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1

    moves = 0
    moves += tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    moves += 1
    moves += tower_of_hanoi(n - 1, auxiliary, destination, source)

    return moves

# Test the function
num_discs = int(input("Enter the number of discs: "))
total_moves = tower_of_hanoi(num_discs, 'Rod 1', 'Rod 3', 'Rod 2')
print(f"\nTotal moves required: {total_moves}")


"""
💡 **Question 7**

Given a string **str**, the task is to print all the permutations of **str**. A **permutation** is an arrangement of all or part of a set of objects, with regard to the order of the arrangement. For instance, the words ‘bat’ and ‘tab’ represents two distinct permutation (or arrangements) of a similar three letter word.

**Examples:**

> Input: str = “cd”
> 
> 
> **Output:** cd dc
> 
> **Input:** str = “abb”
> 
> **Output:** abb abb bab bba bab bba
> 
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
def q7(S):
    permutations(list(S), 0, len(S) - 1)

S = 'XYZ'
q7(S)
"""
💡 **Question 8**

Given a string, count total number of consonants in it. A consonant is an English alphabet character that is not vowel (a, e, i, o and u). Examples of constants are b, c, d, f, and g.

**Examples :**
Input : abc de
Output : 3
There are three consonants b, c and d.

Input : geeksforgeeks portal
Output : 12
"""
def q8(n):
    d={'a':1,'e':1,'i':1,'o':1,'u':1}
    c=0
    for i in n:
        if i not in d:
            c+=1
    return c
n='qwertyu'
print(q8(n))
    