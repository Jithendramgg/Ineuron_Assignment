# Assignment Questions 15

"""
💡 **Question 1**

Given an array **arr[ ]** of size **N** having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.Next greater element of an element in the array is the nearest element on the right which is greater than the current element.If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

**Example 1:**

```
Input:
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ?
since it doesn't exist, it is -1.

```

**Example 2:**

```
Input:
N = 5, arr[] [6 8 0 1 3]
Output:
8 -1 1 3 -1
Explanation:
In the array, the next larger element to
6 is 8, for 8 there is no larger elements
hence it is -1, for 0 it is 1 , for 1 it
is 3 and then for 3 there is no larger
element on right and hence -1.
```

"""
def findNextGreaterElements(arr):
    stack = []
    result = [-1] * len(arr)

    for i, num in enumerate(arr):
        while stack and arr[stack[-1]] < num:
            result[stack.pop()] = num
        stack.append(i)

    return result
arr1 = [1, 3, 2, 4]
print(findNextGreaterElements(arr1))
# Output: [3, 4, 4, -1]

arr2 = [6, 8, 0, 1, 3]
print(findNextGreaterElements(arr2))
# Output: [8, -1, 1, 3, -1]


"""
💡 **Question 2**

Given an array **a** of integers of length **n**, find the nearest smaller number for every element such that the smaller element is on left side.If no small element present on the left print -1.

**Example 1:**

```
Input: n = 3
a = {1, 6, 2}
Output: -1 1 1
Explaination: There is no number at the
left of 1. Smaller number than 6 and 2 is 1.
```

**Example 2:**

```
Input: n = 6
a = {1, 5, 0, 3, 4, 5}
Output: -1 1 -1 0 3 4
Explaination: Upto 3 it is easy to see
the smaller numbers. But for 4 the smaller
numbers are 1, 0 and 3. But among them 3
is closest. Similary for 5 it is 4.
```

"""
def findNearestSmallerElements(a):
    stack = []
    result = [-1] * len(a)

    for i, num in enumerate(a):
        while stack and stack[-1] >= num:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(num)

    return result
a1 = [1, 6, 2]
print(findNearestSmallerElements(a1))
# Output: [-1, 1, 1]

a2 = [1, 5, 0, 3, 4, 5]
print(findNearestSmallerElements(a2))
# Output: [-1, 1, -1, 0, 3, 4]

"""
💡 **Question 3**

Implement a Stack using two queues **q1** and **q2**.

**Example 1:**

```
Input:
push(2)
push(3)
pop()
push(4)
pop()
Output:3 4
Explanation:
push(2) the stack will be {2}
push(3) the stack will be {2 3}
pop()   poped element will be 3 the
        stack will be {2}
push(4) the stack will be {2 4}
pop()   poped element will be 4

```

**Example 2:**

```
Input:
push(2)
pop()
pop()
push(3)
Output:2 -1
```

"""
class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, element):
        self.q1.append(element)

    def pop(self):
        if not self.empty():
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            return self.q1.pop()

    def top(self):
        if not self.empty():
            return self.q1[-1]

    def empty(self):
        return len(self.q1) == 0 and len(self.q2) == 0
stack1 = Stack()
stack1.push(2)
stack1.push(3)
print(stack1.pop())  # Output: 3
stack1.push(4)
print(stack1.pop())  # Output: 4

stack2 = Stack()
stack2.push(2)
print(stack2.pop())  # Output: 2
print(stack2.pop())  # Output: None
stack2.push(3)
print(stack2.top())  # Output: 3

"""
💡 **Question 4**

You are given a stack **St**. You have to reverse the stack using recursion.

**Example 1:**

```
Input:St = {3,2,1,7,6}
Output:{6,7,1,2,3}
```

**Example 2:**

```
Input:St = {4,3,9,6}
Output:{6,9,3,4}
```

"""
def reverseStack(St):
    if not St:
        return

    topElement = St.pop()
    reverseStack(St)
    insertAtBottom(St, topElement)


def insertAtBottom(St, element):
    if not St:
        St.append(element)
        return

    topElement = St.pop()
    insertAtBottom(St, element)
    St.append(topElement)


# Testing the reverseStack function
St1 = [3, 2, 1, 7, 6]
reverseStack(St1)
print(St1)
# Output: [6, 7, 1, 2, 3]

St2 = [4, 3, 9, 6]
reverseStack(St2)
print(St2)
# Output: [6, 9, 3, 4]

"""
💡 **Question 5**

You are given a string **S**, the task is to reverse the string using stack.

**Example 1:**

```
Input: S="GeeksforGeeks"
Output: skeeGrofskeeG
```

"""
def reverseString(S):
    stack = []

    # Push characters onto the stack
    for ch in S:
        stack.append(ch)

    reversedString = ""
    # Pop characters from the stack to form the reversed string
    while stack:
        reversedString += stack.pop()

    return reversedString


# Testing the reverseString function
S1 = "GeeksforGeeks"
print(reverseString(S1))
# Output: skeeGrofskeeG

"""
💡 **Question 6**

Given string **S** representing a postfix expression, the task is to evaluate the expression and find the final value. Operators will only include the basic arithmetic operators like ***, /, + and -**.

**Example 1:**

```
Input: S = "231*+9-"
Output: -4
Explanation:
After solving the given expression,
we have -4 as result.

```

**Example 2:**

```
Input: S = "123+*8-"
Output: -3
Explanation:
After solving the given postfix
expression, we have -3 as result.
```

"""
def evaluatePostfixExpression(S):
    stack = []

    for ch in S:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if ch == '*':
                result = operand1 * operand2
            elif ch == '/':
                result = operand1 / operand2
            elif ch == '+':
                result = operand1 + operand2
            elif ch == '-':
                result = operand1 - operand2

            stack.append(result)

    return stack.pop()


# Testing the evaluatePostfixExpression function
S1 = "231*+9-"
print(evaluatePostfixExpression(S1))
# Output: -4

S2 = "123+*8-"
print(evaluatePostfixExpression(S2))
# Output: -3


"""
💡 **Question 7**

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

**Example 1:**

```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

"""
class MinStack:
    def __init__(self):
        self.dataStack = []
        self.minStack = []

    def push(self, val):
        self.dataStack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self):
        popped = self.dataStack.pop()
        if popped == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        return self.dataStack[-1]

    def getMin(self):
        return self.minStack[-1]


# Testing the MinStack class
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())     # Output: 0
print(minStack.getMin())  # Output: -2

"""
💡 **Question 8**

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:**

!https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

```

**Example 2:**

"""
def trap(height):
    left = 0
    right = len(height) - 1
    leftMax = rightMax = water = 0

    while left <= right:
        if height[left] <= height[right]:
            if height[left] > leftMax:
                leftMax = height[left]
            else:
                water += leftMax - height[left]
            left += 1
        else:
            if height[right] > rightMax:
                rightMax = height[right]
            else:
                water += rightMax - height[right]
            right -= 1

    return water


# Testing the trap function
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
# Output: 6

