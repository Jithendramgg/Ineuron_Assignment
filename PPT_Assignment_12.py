# Assignment Questions 12

"""
💡 **Question 1**

Given a singly linked list, delete **middle** of the linked list. For example, if given linked list is 1->2->**3**->4->5 then linked list should be modified to 1->2->4->5.If there are **even** nodes, then there would be **two middle** nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.If the input linked list is NULL or has 1 node, then it should return NULL

**Example 1:**

```
Input:
LinkedList: 1->2->3->4->5
Output:1 2 4 5

```

**Example 2:**

```
Input:
LinkedList: 2->4->6->7->5->1
Output:2 4 6 5 1
```

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteMiddleNode(head):
    # Base cases: empty list or list with one node
    if not head or not head.next:
        return None

    slow = head
    fast = head
    prev = None

    # Move the fast pointer two steps ahead and the slow pointer one step ahead
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    # Skip the middle node by updating the next pointers
    prev.next = slow.next

    return head
# Function to print the linked list
def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()


# Create the linked list for the first example
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

print("Original Linked List:")
printLinkedList(head1)

head1 = deleteMiddleNode(head1)

printLinkedList(head1)

"""
💡 **Question 2**

Given a linked list of **N** nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

**Example 1:**

```
Input:
N = 3
value[] = {1,3,4}
x(position at which tail is connected) = 2
Output:True
Explanation:In above test case N = 3.
The linked list with nodes N = 3 is
given. Then value of x=2 is given which
means last node is connected with xth
node of linked list. Therefore, there
exists a loop.
```

**Example 2:**

```
Input:
N = 4
value[] = {1,8,3,4}
x = 0
Output:False
Explanation:For N = 4 ,x = 0 means
then lastNode->next = NULL, then
the Linked list does not contains
any loop.
```

"""
# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to check if a linked list has a loop
def hasLoop(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False


# Create a linked list with a loop for the first example
head1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(4)
head1.next = node2
node2.next = node3
node3.next = node2  # Connect the tail to the 2nd node

print("Linked List has loop:", hasLoop(head1))

"""
💡 **Question 3**

Given a linked list consisting of **L** nodes and given a number **N**. The task is to find the **N**th node from the end of the linked list.

**Example 1:**

```
Input:
N = 2
LinkedList: 1->2->3->4->5->6->7->8->9
Output:8
Explanation:In the first example, there
are 9 nodes in linked list and we need
to find 2nd node from end. 2nd node
from end is 8.

```

**Example 2:**

```
Input:
N = 5
LinkedList: 10->5->100->5
Output:-1
Explanation:In the second example, there
are 4 nodes in the linked list and we
need to find 5th from the end. Since 'n'
is more than the number of nodes in the
linked list, the output is -1.
```

"""
# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to find the Nth node from the end of a linked list
def findNthFromEnd(head, n):
    if not head:
        return -1
    
    slow = head
    fast = head
    
    # Move the fast pointer n steps ahead
    for _ in range(n):
        if not fast:
            return -1
        fast = fast.next
    
    # Move both slow and fast pointers until the fast pointer reaches the end
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    
    return slow.val if slow else -1


# Create a linked list for the first example
head1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)
node9 = ListNode(9)
head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9

n1 = 2
print("Nth node from the end:", findNthFromEnd(head1, n1))

"""
💡 **Question 4**

Given a singly linked list of characters, write a function that returns true if the given list is a palindrome, else false.

!https://media.geeksforgeeks.org/wp-content/uploads/20220816144425/LLdrawio.png

**Examples:**

> Input: R->A->D->A->R->NULL
> 
> 
> **Output:** Yes
> 
> **Input:** C->O->D->E->NULL
> 
> **Output:** No
> 
"""
# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to check if a linked list is a palindrome
def isPalindrome(head):
    if not head or not head.next:
        return True
    
    # Find the middle of the linked list
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half of the linked list
    second_half = reverseLinkedList(slow)
    
    # Compare the reversed second half with the first half
    while second_half:
        if head.val != second_half.val:
            return False
        head = head.next
        second_half = second_half.next
    
    return True


# Helper function to reverse a linked list
def reverseLinkedList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


# Create a linked list for the first example
head1 = ListNode('R')
node2 = ListNode('A')
node3 = ListNode('D')
node4 = ListNode('A')
node5 = ListNode('R')
head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Is the linked list a palindrome?", isPalindrome(head1))


"""
💡 **Question 5**

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
# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to remove a loop from the linked list
def removeLoop(head):
    if not head or not head.next:
        return head
    
    # Detect if a loop exists in the linked list
    slow = head.next
    fast = head.next.next
    while fast and fast.next:
        if slow == fast:
            break
        slow = slow.next
        fast = fast.next.next
    
    # If there is no loop, return the head of the linked list
    if slow != fast:
        return head
    
    # Find the start of the loop
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    
    # Remove the loop
    fast.next = None
    
    return head


# Function to create a linked list with a loop
def createLinkedList(arr, x):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    loop_node = None
    
    for i in range(1, len(arr)):
        node = ListNode(arr[i])
        curr.next = node
        curr = node
        if i == x:
            loop_node = node
    
    curr.next = loop_node
    
    return head


# Function to print the linked list
def printLinkedList(head):
    if not head:
        print("Empty linked list")
        return
    
    curr = head
    visited = set()
    while curr:
        if curr in visited:
            print("Loop detected")
            return
        visited.add(curr)
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# Example 1
arr1 = [1, 3, 4]
x1 = 2
head1 = createLinkedList(arr1, x1)

print("Example 1:")
print("Before removing the loop:")
printLinkedList(head1)

removeLoop(head1)

print("After removing the loop:")
printLinkedList(head1)
print()


"""
💡 **Question 6**

Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same till end of the linked list.

Difficulty Level: Rookie

**Examples**:

```
Input:
M = 2, N = 2
Linked List: 1->2->3->4->5->6->7->8
Output:
Linked List: 1->2->5->6

Input:
M = 3, N = 2
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->2->3->6->7->8

Input:
M = 1, N = 1
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->3->5->7->9
```

"""
# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to traverse the linked list and retain M nodes then delete next N nodes
def retainDelete(head, M, N):
    if not head:
        return None
    
    curr = head
    prev = None
    
    while curr:
        # Retain M nodes
        for _ in range(M):
            if not curr:
                return head
            prev = curr
            curr = curr.next
        
        # Delete N nodes
        for _ in range(N):
            if not curr:
                return head
            curr = curr.next
        
        # Update the next pointer of the previous node
        prev.next = curr
    
    return head


# Function to create a linked list from a list of values
def createLinkedList(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    
    for i in range(1, len(arr)):
        node = ListNode(arr[i])
        curr.next = node
        curr = node
    
    return head


# Function to print the linked list
def printLinkedList(head):
    if not head:
        print("Empty linked list")
        return
    
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# Example 1
arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
M1 = 2
N1 = 2
head1 = createLinkedList(arr1)

print("Example 1:")
print("Before retaining and deleting nodes:")
printLinkedList(head1)

head1 = retainDelete(head1, M1, N1)

print("After retaining and deleting nodes:")
printLinkedList(head1)
print()


# Example 2
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
M2 = 3
N2 = 2
head2 = createLinkedList(arr2)

print("Example 2:")
print("Before retaining and deleting nodes:")
printLinkedList(head2)

head2 = retainDelete(head2, M2, N2)

print("After retaining and deleting nodes:")
printLinkedList(head2)
print()


# Example 3
arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
M3 = 1
N3 = 1
head3 = createLinkedList(arr3)

print("Example 3:")
print("Before retaining and deleting nodes:")
printLinkedList(head3)

head3 = retainDelete(head3, M3, N3)

print("After retaining and deleting nodes:")
printLinkedList(head3)

"""
💡 **Question 7**

Given two linked lists, insert nodes of second list into first list at alternate positions of first list.
For example, if first list is 5->7->17->13->11 and second is 12->10->2->4->6, the first list should become 5->12->7->10->17->2->13->4->11->6 and second list should become empty. The nodes of second list should only be inserted when there are positions available. For example, if the first list is 1->2->3 and second list is 4->5->6->7->8, then first list should become 1->4->2->5->3->6 and second list to 7->8.

Use of extra space is not allowed (Not allowed to create additional nodes), i.e., insertion must be done in-place. Expected time complexity is O(n) where n is number of nodes in first list.

"""
# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to insert nodes of the second list into the first list at alternate positions
def insertAlternate(head1, head2):
    if not head1:
        return head2
    
    if not head2:
        return head1
    
    curr1 = head1
    curr2 = head2
    
    while curr1 and curr2:
        next1 = curr1.next
        next2 = curr2.next
        
        curr1.next = curr2
        curr2.next = next1
        
        curr1 = next1
        curr2 = next2
    
    return head1


# Function to create a linked list from a list of values
def createLinkedList(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    
    for i in range(1, len(arr)):
        node = ListNode(arr[i])
        curr.next = node
        curr = node
    
    return head


# Function to print the linked list
def printLinkedList(head):
    if not head:
        print("Empty linked list")
        return
    
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# Example 1
arr1 = [5, 7, 17, 13, 11]
arr2 = [12, 10, 2, 4, 6]
head1 = createLinkedList(arr1)
head2 = createLinkedList(arr2)

print("Example 1:")
print("Before inserting alternate nodes:")
print("First list:")
printLinkedList(head1)
print("Second list:")
printLinkedList(head2)

head1 = insertAlternate(head1, head2)

print("After inserting alternate nodes:")
print("First list:")
printLinkedList(head1)
print("Second list:")
printLinkedList(head2)
print()


# Example 2
arr3 = [1, 2, 3]
arr4 = [4, 5, 6, 7, 8]
head3 = createLinkedList(arr3)
head4 = createLinkedList(arr4)

print("Example 2:")
print("Before inserting alternate nodes:")
print("First list:")
printLinkedList(head3)
print("Second list:")
printLinkedList(head4)

head3 = insertAlternate(head3, head4)

print("After inserting alternate nodes:")
print("First list:")
printLinkedList(head3)
print("Second list:")
printLinkedList(head4)

"""
💡 **Question 8**

Given a singly linked list, find if the linked list is [circular](https://www.geeksforgeeks.org/circular-linked-list/amp/) or not.

> A linked list is called circular if it is not NULL-terminated and all nodes are connected in the form of a cycle. Below is an example of a circular linked list.
> 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d30bbf79-b1eb-4ba4-b23e-6d3f27ccdfe5/Untitled.png)

"""
# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to determine if a linked list is circular or not
def isCircular(head):
    if not head:
        return False
    
    slow = head
    fast = head.next
    
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    
    return False


# Function to create a circular linked list
def createCircularLinkedList(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    
    for i in range(1, len(arr)):
        node = ListNode(arr[i])
        curr.next = node
        curr = node
    
    curr.next = head
    
    return head


# Example 1
arr1 = [1, 2, 3, 4, 5]
head1 = createCircularLinkedList(arr1)

print("Example 1:")
print("Linked list is circular:", isCircular(head1))
print()


# Example 2
arr2 = [1, 2, 3, 4, 5]
head2 = ListNode(arr2[0])
curr2 = head2

for i in range(1, len(arr2)):
    node = ListNode(arr2[i])
    curr2.next = node
    curr2 = node

print("Example 2:")
print("Linked list is circular:", isCircular(head2))
