---
difficulty: Medium
tags:
    - Array
    - Divide and Conquer
    - Dynamic Programming
---

<!-- problem:start -->

# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray)

## Description

<!-- description:start -->

<p>Given an integer array <code>nums</code>, find the <span data-keyword="subarray-nonempty">subarray</span> with the largest sum, and return <em>its sum</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The subarray [4,-1,2,1] has the largest sum 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> The subarray [1] has the largest sum 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23
<strong>Explanation:</strong> The subarray [5,4,-1,7,8] has the largest sum 23.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution using the <strong>divide and conquer</strong> approach, which is more subtle.</p>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution -> Kadane’s Algorithm

Kadane’s Algorithm is a famous and efficient algorithm used to solve the Maximum Subarray Problem — that is, to find the contiguous subarray with the maximum sum within a one-dimensional array of numbers.

### Kadane’s Algorithm Walkthrough

Given: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`

### Initialization:
`current_sum = max_sum = nums[0] = -2`

### Step-by-step:

| num  | current_sum                  | max_sum         |
|------|------------------------------|-----------------|
| 1    | max(1, -2 + 1) = **1**       | max(-2, 1) = **1**  |
| -3   | max(-3, 1 + (-3)) = **-2**   | max(1, -2) = **1**  |
| 4    | max(4, -2 + 4) = **4**       | max(1, 4) = **4**   |
| -1   | max(-1, 4 + (-1)) = **3**    | max(4, 3) = **4**   |
| 2    | max(2, 3 + 2) = **5**        | max(4, 5) = **5**   |
| 1    | max(1, 5 + 1) = **6**        | max(5, 6) = **6**   |
| -5   | max(-5, 6 + (-5)) = **1**    | max(6, 1) = **6**   |
| 4    | max(4, 1 + 4) = **5**        | max(6, 5) = **6**   |


#### Python3

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]
        
        for num in nums [1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
```
