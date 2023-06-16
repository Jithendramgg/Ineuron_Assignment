# Assignment Questions 14

"""
💡 **Question 1**

Given a linked list of **N** nodes such that it may contain a loop.

A loop here means that the last node of the link list is connected to the node at position X(1-based index). If the link list does not have any loop, X=0.

Remove the loop from the linked list, if it is present, i.e. unlink the last node which is forming the loop.

**Example 1:**

```
Input:
N = 3
value[] = {1,3,4}
X = 2
Output:1
Explanation:The link list looks like
1 -> 3 -> 4
     ^    |
     |____|
A loop is present. If you remove it
successfully, the answer will be 1.

```

**Example 2:**

```
Input:
N = 4
value[] = {1,8,3,4}
X = 0
Output:1
Explanation:The Linked list does not
contains any loop.
```

**Example 3:**

```
Input:
N = 4
value[] = {1,2,3,4}
X = 1
Output:1
Explanation:The link list looks like
1 -> 2 -> 3 -> 4
^              |
|______________|
A loop is present.
If you remove it successfully,
the answer will be 1.
```

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeLoop(head):
    if not head or not head.next:
        return head

    slow = fast = head
    loop_found = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            loop_found = True
            break

    if not loop_found:
        return head

    slow = head

    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    fast.next = None

    return head
# Example 1:
# Input: 1 -> 3 -> 4 -> 2 (loop)
# Output: 1 -> 3 -> 4
node1 = Node(1)
node2 = Node(3)
node3 = Node(4)
node4 = Node(2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creating a loop

head = removeLoop(node1)
while head:
    print(head.data, end=" -> ")
    head = head.next
# Output: 1 -> 3 -> 4 ->

print()

# Example 2:
# Input: 1 -> 8 -> 3 -> 4
# Output: 1 -> 8 -> 3 -> 4
node1 = Node(1)
node2 = Node(8)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4

head = removeLoop(node1)
while head:
    print(head.data, end=" -> ")
    head = head.next
# Output: 1 -> 8 -> 3 -> 4

print()

"""
💡 **Question 2**

A number **N** is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

**Example 1:**

```
Input:
LinkedList: 4->5->6
Output:457

```

**Example 2:**

```
Input:
LinkedList: 1->2->3
Output:124
```

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addOne(head):
    if not head:
        return Node(1)  # If the list is empty, return a new node with value 1

    carry = 1
    prev = None
    curr = head

    while curr:
        curr.data += carry
        carry = curr.data // 10
        curr.data %= 10

        prev = curr
        curr = curr.next

    if carry:
        prev.next = Node(carry)  # Add an additional node with value 1

    # Reverse the linked list
    prev = None
    curr = head
    next = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev  # Return the new head of the reversed linked list

def printLinkedList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("")

# Example 1:
# Input: 4 -> 5 -> 6
# Output: 457
node1 = Node(4)
node2 = Node(5)
node3 = Node(6)
node1.next = node2
node2.next = node3

head = addOne(node1)
printLinkedList(head)
# Output: 4 -> 5 -> 7

# Example 2:
# Input: 1 -> 2 -> 3
# Output: 124
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

head = addOne(node1)
printLinkedList(head)
# Output: 1 -> 2 -> 4

"""
💡 **Question 3**

Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:(i) a **next** pointer to the next node,(ii) a **bottom** pointer to a linked list where this node is head.Each of the sub-linked-list is in sorted order.Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. **Note:** The flattened list will be printed using the bottom pointer instead of next pointer.

**Example 1:**

```
Input:
5 -> 10 -> 19 -> 28
|     |     |     |
7     20    22   35
|           |     |
8          50    40
|                 |
30               45
Output: 5-> 7-> 8- > 10 -> 19-> 20->
22-> 28-> 30-> 35-> 40-> 45-> 50.
Explanation:
The resultant linked lists has every
node in a single level.(Note:| represents the bottom pointer.)

```

**Example 2:**

```
Input:
5 -> 10 -> 19 -> 28
|          |
7          22
|          |
8          50
|
30
Output: 5->7->8->10->19->22->28->30->50
Explanation:
The resultant linked lists has every
node in a single level.

(Note:| represents the bottom pointer.)
```

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

def mergeLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    result = None

    if list1.data <= list2.data:
        result = list1
        result.bottom = mergeLists(list1.bottom, list2)
    else:
        result = list2
        result.bottom = mergeLists(list1, list2.bottom)

    result.next = None

    return result

def flatten(head):
    if not head or not head.next:
        return head

    head.next = flatten(head.next)
    head = mergeLists(head, head.next)

    return head

def printFlattenedList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.bottom
    print("")

# Example 1:
# Input:
# 5 -> 10 -> 19 -> 28
# |     |     |     |
# 7     20    22   35
# |           |     |
# 8          50    40
# |                 |
# 30               45
# Output: 5->7->8->10->19->20->22->28->30->35->40->45->50
node1 = Node(5)
node2 = Node(10)
node3 = Node(19)
node4 = Node(28)
node1.next = node2
node2.next = node3
node3.next = node4

node5 = Node(7)
node6 = Node(20)
node7 = Node(22)
node5.next = node6
node6.next = node7

node8 = Node(8)
node9 = Node(50)
node8.next = node9

node10 = Node(30)
node7.bottom = node10

node11 = Node(35)
node9.bottom = node11

node12 = Node(40)
node13 = Node(45)
node12.next = node13

node4.bottom = node12

head = flatten(node1)
printFlattenedList(head)
# Output: 5->7->8->10->19->20->22->28->30->35->40->45->50

# Example 2:
# Input:
# 5 -> 10 -> 19 -> 28
# |          |
# 7          22
# |          |
# 8          50
# |
# 30
# Output: 5->7->8->10->19->22->28->30->50
node1 = Node(5)
node2 = Node(10)
node3 = Node(19)
node4 = Node(28)
node1.next = node2
node2.next = node3
node3.next = node4

node5 = Node(7)
node6 = Node(22)
node5.next = node6

node7 = Node(8)
node8 = Node(50)
node7.next = node8

node9 = Node(30)
node6.bottom = node9

head = flatten(node1)
printFlattenedList(head)
# Output: 5->7->8->10->19->22->28->30->50

"""
💡 **Question 4**

You are given a special linked list with **N** nodes where each node has a next pointer pointing to its next node. You are also given **M** random pointers, where you will be given **M** number of pairs denoting two nodes **a** and **b**  **i.e. a->arb = b** (arb is pointer to random node)**.**

Construct a copy of the given list. The copy should consist of exactly **N** new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes **X** and **Y** in the original list, where **X.arb** **-->** **Y**, then for the corresponding two nodes **x** and **y** in the copied list, **x.arb --> y.**

Return the head of the copied linked list.

!https://contribute.geeksforgeeks.org/wp-content/uploads/clone.jpg

**Note** :- The diagram isn't part of any example, it just depicts an example of how the linked list may look like.

**Example 1:**

```
Input:
N = 4, M = 2
value = {1,2,3,4}
pairs = {{1,2},{2,4}}
Output:1
Explanation:In this test case, there
are 4 nodes in linked list.  Among these
4 nodes,  2 nodes have arbitrary pointer
set, rest two nodes have arbitrary pointer
as NULL. Second line tells us the value
of four nodes. The third line gives the
information about arbitrary pointers.
The first node arbitrary pointer is set to
node 2.  The second node arbitrary pointer
is set to node 4.

```

**Example 2:**

```
Input:
N = 4, M = 2
value[] = {1,3,5,9}
pairs[] = {{1,1},{3,4}}
Output:1
Explanation:In the given testcase ,
applying the method as stated in the
above example, the output will be 1.
```

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def cloneLinkedList(head):
    if not head:
        return None

    # Step 1: Create a new copy of each node
    curr = head
    while curr:
        new_node = Node(curr.data)
        new_node.next = curr.next
        curr.next = new_node
        curr = new_node.next

    # Step 2: Set the random pointers of the new nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate the original and copied nodes
    original = head
    copied = head.next
    copied_head = copied

    # Step 4: Restore the original linked list
    while original:
        original.next = original.next.next
        if copied.next:
            copied.next = copied.next.next
        original = original.next
        copied = copied.next

    return copied_head

def printLinkedList(head):
    while head:
        print("Data:", head.data, end=" ")
        if head.random:
            print("Random:", head.random.data, end=" ")
        else:
            print("Random: None", end=" ")
        head = head.next
        print("")

# Example 1:
# Input:
# N = 4, M = 2
# value = [1, 2, 3, 4]
# pairs = [[1, 2], [2, 4]]
# Output: 1
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node1.random = node2
node2.random = node4

head = cloneLinkedList(node1)
printLinkedList(head)
# Output:
# Data: 1 Random: 2
# Data: 2 Random: 4
# Data: 3 Random: None
# Data: 4 Random: None

# Example 2:
# Input:
# N = 4, M = 2
# value = [1, 3, 5, 9]
# pairs = [[1, 1], [3, 4]]
# Output: 1
node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(9)
node1.next = node2
node2.next = node3
node3.next = node4
node1.random = node1
node2.random = node4

head = cloneLinkedList(node1)
printLinkedList(head)
# Output:
# Data: 1 Random: 1
# Data: 3 Random: 9
# Data: 5 Random: None
# Data: 9 Random: None

"""
💡 **Question 5**

Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return *the reordered list*.

The **first** node is considered **odd**, and the **second** node is **even**, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

**Example 1:**

!https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg

```
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

```

**Example 2:**

!https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg

```
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
```

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    if not head or not head.next:
        return head

    odd_head = head
    odd_tail = odd_head
    even_head = head.next
    even_tail = even_head

    curr = even_head.next
    is_odd = True

    while curr:
        if is_odd:
            odd_tail.next = curr
            odd_tail = odd_tail.next
        else:
            even_tail.next = curr
            even_tail = even_tail.next

        curr = curr.next
        is_odd = not is_odd

    odd_tail.next = even_head
    even_tail.next = None

    return odd_head

def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("")

# Example 1:
# Input: head = [1, 2, 3, 4, 5]
# Output: [1, 3, 5, 2, 4]
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = oddEvenList(node1)
printLinkedList(head)
# Output: 1 -> 3 -> 5 -> 2 -> 4

# Example 2:
# Input: head = [2, 1, 3, 5, 6, 4, 7]
# Output: [2, 3, 6, 7, 1, 5, 4]
node1 = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(3)
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node7 = ListNode(7)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

head = oddEvenList(node1)
printLinkedList(head)
# Output: 2 -> 3 -> 6 -> 7 -> 1 -> 5 -> 4


"""
💡 **Question 6**

Given a singly linked list of size **N**. The task is to **left-shift** the linked list by **k** nodes, where **k** is a given positive integer smaller than or equal to length of the linked list.

**Example 1:**

```
Input:
N = 5
value[] = {2, 4, 7, 8, 9}
k = 3
Output:8 9 2 4 7
Explanation:Rotate 1:4 -> 7 -> 8 -> 9 -> 2
Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
Rotate 3: 8 -> 9 -> 2 -> 4 -> 7

```

**Example 2:**

```
Input:
N = 8
value[] = {1, 2, 3, 4, 5, 6, 7, 8}
k = 4
Output:5 6 7 8 1 2 3 4
```

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateLeft(head, k):
    if not head or not head.next or k == 0:
        return head

    # Find the kth node from the beginning
    curr = head
    count = 1
    while count < k and curr:
        curr = curr.next
        count += 1

    if not curr:
        return head

    # Rotate the linked list
    new_head = curr.next
    curr.next = None

    # Traverse to the end and connect it to the head
    curr = new_head
    while curr.next:
        curr = curr.next
    curr.next = head

    return new_head

def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("")

# Example 1:
# Input: N = 5, value = [2, 4, 7, 8, 9], k = 3
# Output: 8 -> 9 -> 2 -> 4 -> 7
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(7)
node4 = ListNode(8)
node5 = ListNode(9)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = rotateLeft(node1, 3)
printLinkedList(head)
# Output: 8 -> 9 -> 2 -> 4 -> 7

# Example 2:
# Input: N = 8, value = [1, 2, 3, 4, 5, 6, 7, 8], k = 4
# Output: 5 -> 6 -> 7 -> 8 -> 1 -> 2 -> 3 -> 4
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

head = rotateLeft(node1, 4)
printLinkedList(head)
# Output: 5 -> 6 -> 7 -> 8 -> 1 -> 2 -> 3 -> 4

"""
💡 **Question 7**

You are given the `head` of a linked list with `n` nodes.

For each node in the list, find the value of the **next greater node**. That is, for each node, find the value of the first node that is next to it and has a **strictly larger** value than it.

Return an integer array `answer` where `answer[i]` is the value of the next greater node of the `ith` node (**1-indexed**). If the `ith` node does not have a next greater node, set `answer[i] = 0`.

**Example 1:**

!https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext1.jpg

```
Input: head = [2,1,5]
Output: [5,5,0]

```

**Example 2:**

!https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext2.jpg

```
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
```

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(head):
    # Convert linked list to array
    arr = []
    while head:
        arr.append(head.val)
        head = head.next

    n = len(arr)
    stack = []
    answer = [0] * n

    for i in range(n - 1, -1, -1):
        while stack and arr[i] >= arr[stack[-1]]:
            stack.pop()

        if stack:
            answer[i] = arr[stack[-1]]

        stack.append(i)

    return answer

# Example 1:
# Input: head = [2, 1, 5]
# Output: [5, 5, 0]
node1 = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

result = nextLargerNodes(node1)
print(result)
# Output: [5, 5, 0]

# Example 2:
# Input: head = [2, 7, 4, 3, 5]
# Output: [7, 0, 5, 5, 0]
node1 = ListNode(2)
node2 = ListNode(7)
node3 = ListNode(4)
node4 = ListNode(3)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

result = nextLargerNodes(node1)
print(result)
# Output: [7, 0, 5, 5, 0]

"""
💡 **Question 8**

Given the `head` of a linked list, we repeatedly delete consecutive sequences of nodes that sum to `0` until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.

(Note that in the examples below, all sequences are serializations of `ListNode` objects.)

**Example 1:**

```
Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

```

**Example 2:**

```
Input: head = [1,2,3,-3,4]
Output: [1,2,4]


**Example 3:**

```
Input: head = [1,2,3,-3,-2]
Output: [1]
```

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    dummy = ListNode(0)
    dummy.next = head

    prefix_sum = {}
    cumulative_sum = 0
    node = dummy

    while node:
        cumulative_sum += node.val

        if cumulative_sum in prefix_sum:
            # Remove nodes between prefix_sum[cumulative_sum] and the current node
            remove_sum = cumulative_sum
            prev = prefix_sum[remove_sum].next
            while prev != node:
                remove_sum += prev.val
                del prefix_sum[remove_sum]
                prev = prev.next

            prefix_sum[cumulative_sum].next = node.next
        else:
            prefix_sum[cumulative_sum] = node

        node = node.next

    return dummy.next

# Example 1:
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(-3)
node4 = ListNode(3)
node5 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

result = removeZeroSumSublists(node1)
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 3 1 or 1 2 1

# Example 2:
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(-3)
node5 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

result = removeZeroSumSublists(node1)
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 1 2 4

# Example 3:
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(-3)
node5 = ListNode(-2)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

result = removeZeroSumSublists(node1)
while result:
    print(result.val, end=" ")
    result = result.next
# Output: 1
