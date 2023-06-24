# Assignment Questions 19

"""
💡 1. **Merge k Sorted Lists**

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

**Example 1:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

```

**Example 2:**

```
Input: lists = []
Output: []

```

**Example 3:**

```
Input: lists = [[]]
Output: []

```

**Constraints:**

- `k == lists.length`
- `0 <= k <= 10000`
- `0 <= lists[i].length <= 500`
- `-10000 <= lists[i][j] <= 10000`
- `lists[i]` is sorted in **ascending order**.
- The sum of `lists[i].length` will not exceed `10000`.
"""
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # Create a min-heap
    heap = []
    heapq.heapify(heap)

    # Insert the head nodes of each linked list into the min-heap
    for head in lists:
        if head:
            heapq.heappush(heap, (head.val, id(head), head))

    # Create a dummy node as the head of the result linked list
    dummy = ListNode(0)
    curr = dummy

    # Merge the linked lists
    while heap:
        _, _, node = heapq.heappop(heap)  # Pop the node with the minimum value
        curr.next = node
        curr = curr.next

        if node.next:  # If the node has a next node, insert it into the min-heap
            heapq.heappush(heap, (node.next.val, id(node.next), node.next))

    return dummy.next

"""
💡 2. **Count of Smaller Numbers After Self**

Given an integer array `nums`, return *an integer array* `counts` *where* `counts[i]` *is the number of smaller elements to the right of* `nums[i]`.

**Example 1:**

```
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are2 smaller elements (2 and 1).
To the right of 2 there is only1 smaller element (1).
To the right of 6 there is1 smaller element (1).
To the right of 1 there is0 smaller element.

```

**Example 2:**

```
Input: nums = [-1]
Output: [0]

```

**Example 3:**

```
Input: nums = [-1,-1]
Output: [0,0]

```

**Constraints:**

- `1 <= nums.length <= 100000`
- `-10000 <= nums[i] <= 10000`
"""
def countSmaller(nums):
    def mergeSort(arr, start, end):
        if start >= end:
            return [arr[start]], 0
        
        mid = (start + end) // 2
        left, countLeft = mergeSort(arr, start, mid)
        right, countRight = mergeSort(arr, mid + 1, end)
        
        merged = []
        count = countLeft + countRight
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                count += len(left) - i
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged, count
    
    _, counts = mergeSort(nums, 0, len(nums) - 1)
    return counts
print(countSmaller([5, 2, 6, 1]))  # Output: [2, 1, 1, 0]
print(countSmaller([-1]))  # Output: [0]
print(countSmaller([-1, -1]))  # Output: [0, 0]

"""
💡 3. **Sort an Array**

Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem **without using any built-in** functions in `O(nlog(n))` time complexity and with the smallest space complexity possible.

**Example 1:**

```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

```

**Example 2:**

```
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

```

**Constraints:**

- `1 <= nums.length <= 5 * 10000`
- `-5 * 104 <= nums[i] <= 5 * 10000`
"""
def merge(nums, start, mid, end):
    left = nums[start:mid+1]
    right = nums[mid+1:end+1]
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[start+k] = left[i]
            i += 1
        else:
            nums[start+k] = right[j]
            j += 1
        k += 1

    nums[start+k:end+1] = left[i:] + right[j:]

def sortArray(nums):
    def mergeSort(nums, start, end):
        if start < end:
            mid = (start + end) // 2
            mergeSort(nums, start, mid)
            mergeSort(nums, mid+1, end)
            merge(nums, start, mid, end)

    start, end = 0, len(nums) - 1
    mergeSort(nums, start, end)
    return nums
print(sortArray([5, 2, 3, 1]))  # Output: [1, 2, 3, 5]
print(sortArray([5, 1, 1, 2, 0, 0]))  # Output: [0, 0, 1, 1, 2, 5]

"""
💡 4. **Move all zeroes to end of array**

Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).

**Example:**

```
Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
Output : arr[] = {1, 2, 4, 3, 5, 0, 0, 0};

Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
Output : arr[] = {1, 2, 3, 6, 0, 0, 0};
```

"""
def moveZeroes(nums):
    left = right = 0
    n = len(nums)
    
    while left < n:
        if nums[left] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            right += 1
        left += 1
    
    return nums
print(moveZeroes([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]))  # Output: [1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0]
print(moveZeroes([1, 2, 0, 4, 3, 0, 5, 0]))  # Output: [1, 2, 4, 3, 5, 0, 0, 0]
print(moveZeroes([1, 2, 0, 0, 0, 3, 6]))  # Output: [1, 2, 3, 6, 0, 0, 0]

"""
💡 5. **Rearrange array in alternating positive & negative items with O(1) extra space**

Given an **array of positive** and **negative numbers**, arrange them in an **alternate** fashion such that every positive number is followed by a negative and vice-versa maintaining the **order of appearance**. The number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear at the end of the array.

**Examples:**

> Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}
> 
"""
def rearrangeArray(nums):
    positive = 0
    negative = 0
    n = len(nums)

    while positive < n and negative < n:
        # Find next positive number
        while positive < n and nums[positive] < 0:
            positive += 1

        # Find next negative number
        negative = positive + 1
        while negative < n and nums[negative] > 0:
            negative += 1

        # Shift elements between positive and negative pointers
        if positive < n and negative < n:
            nums[positive+1:negative+1], nums[positive] = nums[positive:negative], nums[positive]
            positive += 2

    return nums
print(rearrangeArray([1, 2, 3, -4, -1, 4]))  # Output: [-4, 1, -1, 2, 3, 4]
print(rearrangeArray([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]))  # Output: [-5, 5, -2, 2, -8, 4, 7, 1, 8, 0]

"""
💡 **6. Merge two sorted arrays**

Given two sorted arrays, the task is to merge them in a sorted manner.

**Examples:**

> Input: arr1[] = { 1, 3, 4, 5}, arr2[] = {2, 4, 6, 8} 
Output: arr3[] = {1, 2, 3, 4, 4, 5, 6, 8}

Input: arr1[] = { 5, 8, 9}, arr2[] = {4, 7, 8}
Output: arr3[] = {4, 5, 7, 8, 8, 9}
> 
"""
def mergeSortedArrays(arr1, arr2):
    p1 = p2 = 0
    n1 = len(arr1)
    n2 = len(arr2)
    result = []

    while p1 < n1 and p2 < n2:
        if arr1[p1] <= arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
        else:
            result.append(arr2[p2])
            p2 += 1

    while p1 < n1:
        result.append(arr1[p1])
        p1 += 1

    while p2 < n2:
        result.append(arr2[p2])
        p2 += 1

    return result
print(mergeSortedArrays([1, 3, 4, 5], [2, 4, 6, 8]))  # Output: [1, 2, 3, 4, 4, 5, 6, 8]
print(mergeSortedArrays([5, 8, 9], [4, 7, 8]))  # Output: [4, 5, 7, 8, 8, 9]

"""
💡 7. **Intersection of Two Arrays**

Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must be **unique** and you may return the result in **any order**.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

```

**Example 2:**

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

```

**Constraints:**

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`
"""
def intersection(nums1, nums2):
    set1 = set(nums1)
    intersection = set()
    
    for num in nums2:
        if num in set1:
            intersection.add(num)
    
    return list(intersection)
print(intersection([1, 2, 2, 1], [2, 2]))  # Output: [2]
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [9, 4]

"""
💡 8. **Intersection of Two Arrays II**

Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must appear as many times as it shows in both arrays and you may return the result in **any order**.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

```

**Example 2:**

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

```

**Constraints:**

- `1 <= nums1.length, nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 1000`
"""
def intersect(nums1, nums2):
    freq = {}
    
    for num in nums1:
        freq[num] = freq.get(num, 0) + 1
    
    intersection = []
    
    for num in nums2:
        if num in freq and freq[num] > 0:
            intersection.append(num)
            freq[num] -= 1
    
    return intersection
print(intersect([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [4, 9]
