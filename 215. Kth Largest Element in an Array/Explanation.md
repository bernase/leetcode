---
difficulty: Medium
tags:
    - Array
    - Divide and Conquer
    - Sorting
    - Heap (Priority Queue)
	- Quickselect
---

<!-- problem:start -->

# [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description)

## Description

Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Can you solve it without sorting?


**Example 1:**

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2:**

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```


<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

- `1 <= k <= nums.length <= 10⁵`
- `-10⁴ <= nums[i] <= 10⁴`

---

## Intuition

We want the **kth largest element** in the array.  
A naive way is to sort the entire array and pick the element, but sorting costs **O(n log n)**. Since we don’t need the full order, we can solve it more efficiently using either a **min-heap** or the **Quickselect algorithm**.

---

## Approach

### Heap-based
- Maintain a **min-heap** of size `k`.  
- Iterate through the array and push elements into the heap.  
- If the heap exceeds size `k`, remove the smallest element.  
- At the end, the root of the heap (`heap[0]`) is the **kth largest element**.  

This approach is simple and efficient, especially when `k` is small compared to `n`.

### Quickselect
- Pick a pivot (commonly the last element).  
- Partition the array into three groups: `< pivot`, `= pivot`, and `> pivot`.  
- Depending on the index `k`, recurse into the correct partition.  
- Average runtime is **O(n)**, but worst case is **O(n²)** (unlucky pivots).  

Quickselect is faster in practice and uses **O(1)** extra space.

---

## Complexity

| Approach      | Time Complexity       | Space Complexity |
|---------------|-----------------------|------------------|
| Heap (size k) | O(n log k)            | O(k)             |
| Quickselect   | O(n) average, O(n²) worst | O(1)         |

---

## Solution code

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickSelect(l, r):
            less, equal, greater, pivot = l, l, r, nums[r]
            while equal <= greater:
                while equal <= greater and nums[equal] < pivot:
                    nums[equal], nums[less] = nums[less], nums[equal]
                    less += 1
                    equal += 1
                while equal <= greater and nums[equal] == pivot:
                    equal += 1
                while equal <= greater and nums[equal] > pivot:
                    nums[equal], nums[greater] = nums[greater], nums[equal]
                    greater -= 1
                
            if k > greater:
                return quickSelect(greater + 1, r)
            elif k < less:
                return quickSelect(l, less - 1)
            else:
                return nums[greater]


        return quickSelect(0, len(nums)-1)
```

---

## Conclusion

- Use **Heap** for a straightforward and reliable solution.  
- Use **Quickselect** for the best expected runtime and minimal extra memory.  
- Both outperform sorting the full array (**O(n log n)**).  

---
