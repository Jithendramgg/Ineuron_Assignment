# Assignment Questions 13

"""
💡 **Question 1**

Given two linked list of the same size, the task is to create a new linked list using those linked lists. The condition is that the greater node among both linked list will be added to the new linked list.

**Examples:**

```
Input: list1 = 5->2->3->8
list2 = 1->7->4->5
Output: New list = 5->7->4->8

Input:list1 = 2->8->9->3
list2 = 5->3->6->4
Output: New list = 5->8->9->4
```

"""
# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to create a new linked list using the greater nodes from two lists
def createNewLinkedList(list1, list2):
    # Create a dummy node to represent the head of the new list
    dummy = ListNode()
    curr = dummy
    
    # Iterate through both lists simultaneously
    while list1 and list2:
        # Compare the values of the nodes at the current position
        if list1.val >= list2.val:
            # Create a new node with the greater value
            new_node = ListNode(list1.val)
            list1 = list1.next
        else:
            new_node = ListNode(list2.val)
            list2 = list2.next
        
        # Add the new node to the new linked list
        curr.next = new_node
        curr = curr.next
    
    # Add any remaining nodes from list1 or list2
    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2
    
    return dummy.next


# Function to print the values of a linked list
def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()


# Example 1
list1 = ListNode(5)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(8)

list2 = ListNode(1)
list2.next = ListNode(7)
list2.next.next = ListNode(4)
list2.next.next.next = ListNode(5)

print("Example 1:")
new_list = createNewLinkedList(list1, list2)
printLinkedList(new_list)
print()


# Example 2
list3 = ListNode(2)
list3.next = ListNode(8)
list3.next.next = ListNode(9)
list3.next.next.next = ListNode(3)

list4 = ListNode(5)
list4.next = ListNode(3)
list4.next.next = ListNode(6)
list4.next.next.next = ListNode(4)

print("Example 2:")
new_list2 = createNewLinkedList(list3, list4)
printLinkedList(new_list2)

"""
💡 **Question 2**

Write a function that takes a list sorted in non-decreasing order and deletes any duplicate nodes from the list. The list should only be traversed once.

For example if the linked list is 11->11->11->21->43->43->60 then removeDuplicates() should convert the list to 11->21->43->60.

**Example 1:**

```
Input:
LinkedList: 
11->11->11->21->43->43->60
Output:
11->21->43->60
```

**Example 2:**

```
Input:
LinkedList: 
10->12->12->25->25->25->34
Output:
10->12->25->34
```

"""
# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to remove duplicate nodes from a sorted linked list
def removeDuplicates(head):
    # Check if the list is empty or has only one node
    if not head or not head.next:
        return head
    
    # Pointer to iterate through the list
    curr = head

    # Traverse the list and remove duplicates
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return head


# Function to print the values of a linked list
def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()


# Example 1
list1 = ListNode(11)
list1.next = ListNode(11)
list1.next.next = ListNode(11)
list1.next.next.next = ListNode(21)
list1.next.next.next.next = ListNode(43)
list1.next.next.next.next.next = ListNode(43)
list1.next.next.next.next.next.next = ListNode(60)

print("Example 1:")
print("Before removing duplicates:")
printLinkedList(list1)

removeDuplicates(list1)

print("After removing duplicates:")
printLinkedList(list1)
print()


# Example 2
list2 = ListNode(10)
list2.next = ListNode(12)
list2.next.next = ListNode(12)
list2.next.next.next = ListNode(25)
list2.next.next.next.next = ListNode(25)
list2.next.next.next.next.next = ListNode(25)
list2.next.next.next.next.next.next = ListNode(34)

print("Example 2:")
print("Before removing duplicates:")
printLinkedList(list2)

removeDuplicates(list2)

print("After removing duplicates:")
printLinkedList(list2)

"""
💡 **Question 3**

Given a linked list of size **N**. The task is to reverse every **k** nodes (where k is an input to the function) in the linked list. If the number of nodes is not a multiple of *k* then left-out nodes, in the end, should be considered as a group and must be reversed (See Example 2 for clarification).

**Example 1:**

```
Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output:4 2 2 1 8 7 6 5
Explanation:
The first 4 elements 1,2,2,4 are reversed first
and then the next 4 elements 5,6,7,8. Hence, the
resultant linked list is 4->2->2->1->8->7->6->5.

```

**Example 2:**

```
Input:
LinkedList: 1->2->3->4->5
K = 3
Output:3 2 1 5 4
Explanation:
The first 3 elements are 1,2,3 are reversed
first and then elements 4,5 are reversed.Hence,
the resultant linked list is 3->2->1->5->4.
```

"""
# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to reverse every k nodes in a linked list
def reverseKNodes(head, k):
    if not head or not head.next or k == 1:
        return head

    count = 0
    prev = None
    curr = head
    next = None

    # Reverse the first k nodes
    while curr and count < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1

    # Recursively reverse the remaining linked list starting from curr
    if next:
        head.next = reverseKNodes(next, k)

    return prev


# Function to print the values of a linked list
def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()


# Example 1
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(2)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)
list1.next.next.next.next.next = ListNode(6)
list1.next.next.next.next.next.next = ListNode(7)
list1.next.next.next.next.next.next.next = ListNode(8)

print("Example 1:")
print("Before reversing k nodes:")
printLinkedList(list1)

k = 4
reversed_list = reverseKNodes(list1, k)

print("After reversing k nodes:")
printLinkedList(reversed_list)
print()


# Example 2
list2 = ListNode(1)
list2.next = ListNode(2)
list2.next.next = ListNode(3)
list2.next.next.next = ListNode(4)
list2.next.next.next.next = ListNode(5)

print("Example 2:")
print("Before reversing k nodes:")
printLinkedList(list2)

k = 3
reversed_list = reverseKNodes(list2, k)

print("After reversing k nodes:")
printLinkedList(reversed_list)

"""
💡 **Question 4**

Given a linked list, write a function to reverse every alternate k nodes (where k is an input to the function) in an efficient way. Give the complexity of your algorithm.

**Example:**

```
Inputs:   1->2->3->4->5->6->7->8->9->NULL and k = 3
Output:   3->2->1->4->5->6->9->8->7->NULL.
```

"""
# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to reverse every alternate k nodes in a linked list
def reverseAlternateKNodes(head, k):
    if not head or k <= 1:
        return head

    curr = head
    prev = None
    next_node = None
    count = 0

    # Reverse the first k nodes
    while curr and count < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count += 1

    # Link the reversed k nodes with the next k nodes recursively
    if next_node:
        head.next = next_node
        count = 0
        while count < k - 1 and next_node:
            next_node = next_node.next
            count += 1
        if next_node:
            next_node.next = reverseAlternateKNodes(next_node.next, k)

    return prev


# Function to print the values of a linked list
def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()


# Example
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)
list1.next.next.next.next.next = ListNode(6)
list1.next.next.next.next.next.next = ListNode(7)
list1.next.next.next.next.next.next.next = ListNode(8)
list1.next.next.next.next.next.next.next.next = ListNode(9)

print("Before reversal:")
printLinkedList(list1)

k = 3
reversed_list = reverseAlternateKNodes(list1, k)

print("After reversal:")
printLinkedList(reversed_list)

"""
💡 **Question 5**

Given a linked list and a key to be deleted. Delete last occurrence of key from linked. The list may have duplicates.

**Examples**:

```
Input:   1->2->3->5->2->10, key = 2
Output:  1->2->3->5->10
```

"""
# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to delete the last occurrence of a key in a linked list
def deleteLastOccurrence(head, key):
    if not head:
        return head

    prev = None
    curr = head
    last_occurrence = None

    # Traverse the linked list to find the last occurrence of the key
    while curr:
        if curr.val == key:
            last_occurrence = curr
            break
        prev = curr
        curr = curr.next
    # If last occurrence is found, perform the deletion
    if last_occurrence:
        # If the last occurrence is the head node
        if last_occurrence == head:
            head = head.next
        else:
            prev.next = last_occurrence.next

    return head


# Function to print the values of a linked list
def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()


# Example
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(5)
list1.next.next.next.next = ListNode(2)
list1.next.next.next.next.next = ListNode(10)

print("Before deletion:")
printLinkedList(list1)

key = 2
updated_list = deleteLastOccurrence(list1, key)

print("After deletion:")
printLinkedList(updated_list)


"""
💡 **Question 6**

Given two sorted linked lists consisting of **N** and **M** nodes respectively. The task is to merge both of the lists (in place) and return the head of the merged list.

**Examples:**

Input: a: 5->10->15, b: 2->3->20

Output: 2->3->5->10->15->20

Input: a: 1->1, b: 2->4

Output: 1->1->2->4

"""
# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to merge two sorted linked lists in place
def mergeTwoLists(a, b):
    # Initialize a dummy node and current node
    dummy = ListNode(0)
    curr = dummy

    # Compare the values of nodes from both linked lists
    while a and b:
        if a.val <= b.val:
            curr.next = a
            a = a.next
        else:
            curr.next = b
            b = b.next
        curr = curr.next

    # Attach the remaining nodes of the non-empty list
    if a:
        curr.next = a
    if b:
        curr.next = b

    return dummy.next


# Function to print the values of a linked list
def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()


# Example
list1 = ListNode(5)
list1.next = ListNode(10)
list1.next.next = ListNode(15)

list2 = ListNode(2)
list2.next = ListNode(3)
list2.next.next = ListNode(20)

print("List 1:")
printLinkedList(list1)

print("List 2:")
printLinkedList(list2)

merged_list = mergeTwoLists(list1, list2)

print("Merged List:")
printLinkedList(merged_list)

"""
💡 **Question 7**

Given a **Doubly Linked List**, the task is to reverse the given Doubly Linked List.

**Example:**

```
Original Linked list 10 8 4 2
Reversed Linked list 2 4 8 10
```

"""
# Definition for a doubly-linked list node
class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


# Function to reverse a doubly linked list
def reverseLinkedList(head):
    prev = None
    current = head

    # Traverse the linked list
    while current:
        # Swap prev and next pointers of the current node
        current.next, current.prev = current.prev, current.next

        # Move prev to the current node
        prev = current

        # Move current to the next node
        current = current.prev

    # Update the head pointer
    head = prev

    return head


# Function to print the values of a doubly linked list
def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()


# Example
list1 = ListNode(10)
list1.next = ListNode(8)
list1.next.prev = list1
list1.next.next = ListNode(4)
list1.next.next.prev = list1.next
list1.next.next.next = ListNode(2)
list1.next.next.next.prev = list1.next.next

print("Original Linked List:")
printLinkedList(list1)

reversed_list = reverseLinkedList(list1)

print("Reversed Linked List:")
printLinkedList(reversed_list)

"""
💡 **Question 8**

Given a doubly linked list and a position. The task is to delete a node from given position in a doubly linked list.

**Example 1:**

```
Input:
LinkedList = 1 <--> 3 <--> 4
x = 3
Output:1 3
Explanation:After deleting the node at
position 3 (position starts from 1),
the linked list will be now as 1->3.

```

**Example 2:**

```
Input:
LinkedList = 1 <--> 5 <--> 2 <--> 9
x = 1
Output:5 2 9
```

"""
# Definition for a doubly-linked list node
class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


# Function to delete a node from a given position in a doubly linked list
def deleteNode(head, position):
    # Case 1: Empty list
    if not head:
        return head

    # Case 2: Deleting the first node
    if position == 1:
        new_head = head.next
        if new_head:
            new_head.prev = None
        return new_head

    # Case 3: Deleting a node from a given position
    current = head
    for _ in range(position - 1):
        current = current.next
        if not current:
            return head

    # Update the previous node's next pointer
    current.prev.next = current.next

    # Update the next node's previous pointer
    if current.next:
        current.next.prev = current.prev

    return head


# Function to print the values of a doubly linked list
def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()


# Example
list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.prev = list1
list1.next.next = ListNode(4)
list1.next.next.prev = list1.next

print("Original Linked List:")
printLinkedList(list1)

position = 3
updated_list = deleteNode(list1, position)

print("Linked List after deleting position", position)
printLinkedList(updated_list)
