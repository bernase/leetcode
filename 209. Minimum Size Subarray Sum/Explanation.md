---
difficulty: Medium
tags:
    - Array
    - Binary Search
    - Sliding Window
    - Prefix Sum
---

<!-- problem:start -->

# [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/description/)

## Description

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray `[nums_l, nums_{l+1}, ..., nums_r]` of which the sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

**Example 1:**

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

**Example 2:**

```
Input: target = 4, nums = [1,4,4]
Output: 1
```

**Example 3:**

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

- `1 <= target <= 10⁹`
- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁴`

---

## Intuition

We want the **shortest subarray** with sum ≥ target.  
Since `nums[i] > 0`, we know sums grow monotonically as we expand the window. This allows two main approaches:

1. **Sliding Window (O(n))** — expand right until sum ≥ target, then shrink left as much as possible.  
2. **Prefix Sum + Binary Search (O(n log n))** — precompute prefix sums and, for each index, use binary search to find the earliest start index that still satisfies the target condition.

---

## Approach 1: Sliding Window

We maintain:

- Two pointers `left`, `right` that define the current window.
- A running sum of that window.
- A variable `res` to track the minimum length found.

Steps:
1. Expand the window by moving `right` and adding `nums[right]`.
2. While the sum ≥ target, update `res`, and shrink from the left (`left += 1`) to try to minimize length.
3. Continue until `right` reaches the end.

---

### Complexity

| Measure | Complexity |
|---------|-------------|
| Time    | O(n) — each element is added/removed at most once |
| Space   | O(1) |

---

### Python Code: Sliding Window

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        curr_sum = 0
        res = n + 1

        for right in range(n):
            curr_sum += nums[right]
            while curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if res == n + 1 else res
```

---

## Approach 2: Prefix Sum + Binary Search

We build a prefix sum array `prefix`, where:

```
prefix[i] = nums[0] + nums[1] + ... + nums[i-1]
```

So the sum of any subarray `nums[j..i-1]` is:

```
prefix[i] - prefix[j]
```

To satisfy sum ≥ target, we need:

```
prefix[j] <= prefix[i] - target
```

Since `prefix` is strictly increasing (nums[i] > 0), we can binary search for the largest valid `j`.

---

### Complexity

| Measure | Complexity |
|---------|-------------|
| Time    | O(n log n) |
| Space   | O(n)       |

---

### Python Code: Prefix + Binary Search

```python
import bisect

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        # Build prefix sums
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        res = n + 1
        for i in range(1, n + 1):
            needed = prefix[i] - target
            # Find rightmost j with prefix[j] <= needed
            j = bisect.bisect_left(prefix, needed + 1, 0, i) - 1
            if j >= 0:
                res = min(res, i - j)

        return 0 if res == n + 1 else res
```

---

## Conclusion

- **Sliding Window**: best solution (O(n)), relies on positivity of `nums[i]`.  
- **Prefix + Binary Search**: alternative (O(n log n)), good to practice prefix sums and binary search.  
