# Assignment Questions 16

"""
💡 **Question 1**

Given an array, for each element find the value of the nearest element to the right which is having a frequency greater than that of the current element. If there does not exist an answer for a position, then make the value ‘-1’.

**Examples:**

```
Input: a[] = [1, 1, 2, 3, 4, 2, 1]
Output : [-1, -1, 1, 2, 2, 1, -1]

Explanation:
Given array a[] = [1, 1, 2, 3, 4, 2, 1]
Frequency of each element is: 3, 3, 2, 1, 1, 2, 3

Lets calls Next Greater Frequency element as NGF
1. For element a[0] = 1 which has a frequency = 3,
   As it has frequency of 3 and no other next element
   has frequency more than 3 so  '-1'
2. For element a[1] = 1 it will be -1 same logic
   like a[0]
3. For element a[2] = 2 which has frequency = 2,
   NGF element is 1 at position = 6  with frequency
   of 3 > 2
4. For element a[3] = 3 which has frequency = 1,
   NGF element is 2 at position = 5 with frequency
   of 2 > 1
5. For element a[4] = 4 which has frequency = 1,
   NGF element is 2 at position = 5 with frequency
   of 2 > 1
6. For element a[5] = 2 which has frequency = 2,
   NGF element is 1 at position = 6 with frequency
   of 3 > 2
7. For element a[6] = 1 there is no element to its
   right, hence -1
```

```
Input : a[] = [1, 1, 1, 2, 2, 2, 2, 11, 3, 3]
Output : [2, 2, 2, -1, -1, -1, -1, 3, -1, -1]
```

"""
def findNearestGreaterFrequency(a):
    stack = []
    frequency = {}
    n = len(a)
    result = [-1] * n

    for i in range(n - 1, -1, -1):
        frequency[a[i]] = frequency.get(a[i], 0) + 1

        while stack and frequency[a[stack[-1]]] <= frequency[a[i]]:
            index = stack.pop()
            if frequency[a[i]] > frequency[a[index]]:
                result[index] = a[i]

        stack.append(i)

    return result


# Testing the findNearestGreaterFrequency function
a = [1, 1, 2, 3, 4, 2, 1]
print(findNearestGreaterFrequency(a))
# Output: [-1, -1, 1, 2, 2, 1, -1]

a = [1, 1, 1, 2, 2, 2, 2, 11, 3, 3]
print(findNearestGreaterFrequency(a))
# Output: [2, 2, 2, -1, -1, -1, -1, 3, -1, -1]

"""
💡 **Question 2**

Given a stack of integers, sort it in ascending order using another temporary stack.

**Examples:**

```
Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]

Input : [3, 5, 1, 4, 2, 8]
Output : [1, 2, 3, 4, 5, 8]
```

"""
def sortStack(stack):
    tempStack = []

    while stack:
        current = stack.pop()

        while tempStack and tempStack[-1] < current:
            stack.append(tempStack.pop())

        tempStack.append(current)

    while tempStack:
        stack.append(tempStack.pop())

    return stack


# Testing the sortStack function
stack = [34, 3, 31, 98, 92, 23]
print(sortStack(stack))
# Output: [3, 23, 31, 34, 92, 98]

stack = [3, 5, 1, 4, 2, 8]
print(sortStack(stack))
# Output: [1, 2, 3, 4, 5, 8]

"""
💡 **Question 3**

Given a stack with **push()**, **pop()**, and **empty()** operations, The task is to delete the **middle** element ****of it without using any additional data structure.

Input  : Stack[] = [1, 2, 3, 4, 5]

Output : Stack[] = [1, 2, 4, 5]

Input  : Stack[] = [1, 2, 3, 4, 5, 6]

Output : Stack[] = [1, 2, 4, 5, 6]

"""
def deleteMiddle(stack):
    if len(stack) == 0:
        return

    middle_index = len(stack) // 2
    deleteMiddleUtil(stack, middle_index)


def deleteMiddleUtil(stack, k):
    if k == 0:
        stack.pop()
        return

    top = stack.pop()
    deleteMiddleUtil(stack, k - 1)
    stack.append(top)


# Testing the deleteMiddle function
stack = [1, 2, 3, 4, 5]
deleteMiddle(stack)
print(stack)
# Output: [1, 2, 4, 5]

stack = [1, 2, 3, 4, 5, 6]
deleteMiddle(stack)
print(stack)
# Output: [1, 2, 4, 5, 6]

"""
💡 **Question 4**

Given a Queue consisting of first **n** natural numbers (in random order). The task is to check whether the given Queue elements can be arranged in increasing order in another Queue using a stack. The operation allowed are:

1. Push and pop elements from the stack
2. Pop (Or Dequeue) from the given Queue.
3. Push (Or Enqueue) in the another Queue.

**Examples :**

Input : Queue[] = { 5, 1, 2, 3, 4 } 

Output : Yes 

Pop the first element of the given Queue 

i.e 5. Push 5 into the stack. 

Now, pop all the elements of the given Queue and push them to second Queue. 

Now, pop element 5 in the stack and push it to the second Queue.   

Input : Queue[] = { 5, 1, 2, 6, 3, 4 } 

Output : No 

Push 5 to stack. 

Pop 1, 2 from given Queue and push it to another Queue. 

Pop 6 from given Queue and push to stack. 

Pop 3, 4 from given Queue and push to second Queue. 

Now, from using any of above operation, we cannot push 5 into the second Queue because it is below the 6 in the stack.

"""
from queue import Queue


def checkIncreasingOrder(queue):
    stack = []
    firstQueue = Queue()
    secondQueue = Queue()

    while not queue.empty():
        element = queue.get()

        if len(stack) == 0 or element > stack[-1]:
            stack.append(element)
        else:
            firstQueue.put(element)

    while not firstQueue.empty():
        secondQueue.put(firstQueue.get())

    while not secondQueue.empty():
        element = secondQueue.get()

        if len(stack) == 0 or element > stack[-1]:
            stack.append(element)
        else:
            return "No"

    return "Yes"


# Testing the function
queue = Queue()

queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
print(checkIncreasingOrder(queue))
# Output: Yes

queue = Queue()
queue.put(5)
queue.put(1)
queue.put(2)
queue.put(6)
queue.put(3)
queue.put(4)
print(checkIncreasingOrder(queue))
# Output: No


"""
💡 **Question 5**

Given a number , write a program to reverse this number using stack.

**Examples:**

```
Input : 365
Output : 563

Input : 6899
Output : 9986
```

"""
def reverseNumber(number):
    number_str = str(number)
    stack = []
    
    # Push digits into the stack
    for digit in number_str:
        stack.append(digit)
    
    reversed_str = ""
    
    # Pop digits from the stack and append to the reversed string
    while stack:
        reversed_str += stack.pop()
    
    # Convert the reversed string back to an integer
    reversed_number = int(reversed_str)
    
    return reversed_number


# Testing the function
number = 365
print(reverseNumber(number))
# Output: 563

number = 6899
print(reverseNumber(number))
# Output: 9986


"""
💡 **Question 6**

Given an integer k and a **[queue](https://www.geeksforgeeks.org/queue-data-structure/)** of integers, The task is to reverse the order of the first **k** elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

- **enqueue(x) :** Add an item x to rear of queue
- **dequeue() :** Remove an item from front of queue
- **size() :** Returns number of elements in queue.
- **front() :** Finds front item.
"""
from queue import Queue


def reverseKElements(queue, k):
    if k <= 0 or k > queue.qsize():
        return queue

    stack = []

    # Dequeue the first k elements and push them onto the stack
    for _ in range(k):
        stack.append(queue.get())

    # Enqueue the elements from the stack back into the queue
    while stack:
        queue.put(stack.pop())

    # Move the remaining elements after k to the rear of the queue
    for _ in range(queue.qsize() - k):
        queue.put(queue.get())

    return queue


# Testing the function
queue = Queue()
queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)

k = 3

reversed_queue = reverseKElements(queue, k)

while not reversed_queue.empty():
    print(reversed_queue.get())
# Output: 3 2 1 4 5

"""
💡 **Question 7**

Given a sequence of n strings, the task is to check if any two similar words come together and then destroy each other then print the number of words left in the sequence after this pairwise destruction.

**Examples:**

Input : ab aa aa bcd ab

Output : 3

*As aa, aa destroys each other so,*

*ab bcd ab is the new sequence.*

Input :  tom jerry jerry tom

Output : 0

*As first both jerry will destroy each other.*

*Then sequence will be tom, tom they will also destroy*

*each other. So, the final sequence doesn’t contain any*

*word.*

"""
def countWords(sequence):
    stack = []

    for word in sequence:
        if stack and stack[-1] == word:
            stack.pop()  # Destroy the matching word
        else:
            stack.append(word)

    return len(stack)


# Testing the function
sequence = ['ab', 'aa', 'aa', 'bcd', 'ab']
result = countWords(sequence)
print("Number of words left:", result)
# Output: 3

sequence = ['tom', 'jerry', 'jerry', 'tom']
result = countWords(sequence)
print("Number of words left:", result)
# Output: 0

"""
💡 **Question 8**

Given an array of integers, the task is to find the maximum absolute difference between the nearest left and the right smaller element of every element in the array.

**Note:** If there is no smaller element on right side or left side of any element then we take zero as the smaller element. For example for the leftmost element, the nearest smaller element on the left side is considered as 0. Similarly, for rightmost elements, the smaller element on the right side is considered as 0.

**Examples:**
0
```
Input : arr[] = {2, 1, 8}
Output : 1
Left smaller  LS[] {0, 0, 1}
Right smaller RS[] {1, 0, 0}
Maximum Diff of abs(LS[i] - RS[i]) = 1

Input  : arr[] = {2, 4, 8, 7, 7, 9, 3}
Output : 4
Left smaller   LS[] = {0, 2, 4, 4, 4, 7, 2}
Right smaller  RS[] = {0, 3, 7, 3, 3, 3, 0}
Maximum Diff of abs(LS[i] - RS[i]) = 7 - 3 = 4

Input : arr[] = {5, 1, 9, 2, 5, 1, 7}
Output : 1
```

"""
def maxAbsDiff(arr):
    n = len(arr)
    leftSmaller = [0] * n
    rightSmaller = [0] * n

    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            rightSmaller[stack.pop()] = arr[i]
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            leftSmaller[stack.pop()] = arr[i]
        stack.append(i)

    maxDiff = 0
    for i in range(n):
        diff = abs(leftSmaller[i] - rightSmaller[i])
        maxDiff = max(maxDiff, diff)

    return maxDiff


# Testing the function
arr = [2, 1, 8]
result = maxAbsDiff(arr)
print("Maximum absolute difference:", result)
# Output: 1

arr = [2, 4, 8, 7, 7, 9, 3]
result = maxAbsDiff(arr)
print("Maximum absolute difference:", result)
# Output: 4

arr = [5, 1, 9, 2, 5, 1, 7]
result = maxAbsDiff(arr)
print("Maximum absolute difference:", result)
# Output: 1
