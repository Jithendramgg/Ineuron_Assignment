# Assignment Questions 20

"""
💡 Question-1

Given a binary tree, your task is to find subtree with maximum sum in tree.

Examples:

Input1 :       

       1

     /   \

   2      3

  / \    / \

4   5  6   7

Output1 : 28

As all the tree elements are positive, the largest subtree sum is equal to sum of all tree elements.

Input2 :

       1

     /    \

  -2      3

  / \    /  \

4   5  -6   2

Output2 : 7

Subtree with largest sum is :

 -2

 / \

4   5

Also, entire tree sum is also 7.

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findMaxSubtreeSum(node):
    if node is None:
        return 0
    
    leftSum = findMaxSubtreeSum(node.left)
    rightSum = findMaxSubtreeSum(node.right)
    
    currentSum = node.value + leftSum + rightSum
    return max(currentSum, leftSum, rightSum)

def traverse(node):
    if node is None:
        return 0
    
    leftSum = findMaxSubtreeSum(node.left)
    rightSum = findMaxSubtreeSum(node.right)
    
    currentSum = node.value + leftSum + rightSum
    global maxSum
    maxSum = max(maxSum, currentSum)
    
    traverse(node.left)
    traverse(node.right)
    
    return currentSum

# Test the algorithm with the given examples
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)

maxSum = float('-inf')
traverse(root1)
print("Output1:", maxSum)

root2 = Node(1)
root2.left = Node(-2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.right.left = Node(-6)
root2.right.right = Node(2)

maxSum = float('-inf')
traverse(root2)
print("Output2:", maxSum)

"""
💡 Question-2

Construct the BST (Binary Search Tree) from its given level order traversal.

Example:

Input: arr[] = {7, 4, 12, 3, 6, 8, 1, 5, 10}

Output: BST:

            7

         /    \

       4     12

     /  \     /

    3   6  8

   /    /     \

 1    5      10

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def constructBST(levelOrder):
    if not levelOrder:
        return None
    
    queue = []
    root = Node(levelOrder[0])
    queue.append(root)
    
    i = 1
    while i < len(levelOrder):
        node = queue.pop(0)
        
        leftSubtree = []
        rightSubtree = []
        
        while i < len(levelOrder) and levelOrder[i] < node.value:
            leftSubtree.append(levelOrder[i])
            i += 1
        
        while i < len(levelOrder) and levelOrder[i] > node.value:
            rightSubtree.append(levelOrder[i])
            i += 1
        
        if leftSubtree:
            node.left = constructBST(leftSubtree)
        
        if rightSubtree:
            node.right = constructBST(rightSubtree)
        
        for element in leftSubtree + rightSubtree:
            queue.append(Node(element))
    
    return root

def printBST(root):
    if root:
        printBST(root.left)
        print(root.value)
        printBST(root.right)

# Test the algorithm with the given example
levelOrder = [7, 4, 12, 3, 6, 8, 1, 5, 10]
root = constructBST(levelOrder)
print("BST:")
printBST(root)

"""
💡 Question-3

Given an array of size n. The problem is to check whether the given array can represent the level order traversal of a Binary Search Tree or not.

Examples:

Input1 : arr[] = {7, 4, 12, 3, 6, 8, 1, 5, 10}

Output1 : Yes

For the given arr[], the Binary Search Tree is:

            7

         /    \

       4     12

     /  \     /

    3   6  8

   /    /     \

 1    5      10

Input2 : arr[] = {11, 6, 13, 5, 12, 10}

Output2 : No

The given arr[] does not represent the level order traversal of a BST.

"""

def isLevelOrderBST(arr):
    if len(arr) <= 1:
        return True
    
    leftSubtree = []
    rightSubtree = []
    
    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            leftSubtree.append(arr[i])
        else:
            break
    
    for j in range(i, len(arr)):
        if arr[j] >= arr[0]:
            return False
        else:
            rightSubtree.append(arr[j])
    
    left = isLevelOrderBST(leftSubtree)
    right = isLevelOrderBST(rightSubtree)
    
    return left and right

# Test the algorithm with the given examples
arr1 = [7, 4, 12, 3, 6, 8, 1, 5, 10]
result1 = isLevelOrderBST(arr1)
print("Output1:", "Yes" if result1 else "No")

arr2 = [11, 6, 13, 5, 12, 10]
result2 = isLevelOrderBST(arr2)
print("Output2:", "Yes" if result2 else "No")
