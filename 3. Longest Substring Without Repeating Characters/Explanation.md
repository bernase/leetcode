---
difficulty: Medium
tags:
    - Hash Table
    - String
    - Sliding Window
---

<!-- problem:start -->

# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description)

## Description

Given a string `s`, find the length of the **longest substring** without repeating characters.

**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
```

**Example 4:**

```
Input: s = ""
Output: 0
```


<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

- `0 <= s.length <= 5 * 10⁴`  
- `s` consists of English letters, digits, symbols and spaces.

---

## Intuition

We want to find the longest contiguous substring in which **no character repeats**.  

A common and efficient way to do this is with the **sliding window** technique: maintain a window (substring) defined by two pointers, expand it when possible, and shrink it when necessary (when there’s a repetition). Use a data structure to check fast whether a character is already in the window.


### Approach: Sliding Window + Set

We maintain:

- Two pointers, `l` (left) and `r` (right), that define the current window: `s[l..r]`.  
- A set (`charSet`) containing the distinct characters in the current window (so we can detect duplicates quickly).  
- A variable `res` to keep track of the **maximum window size** seen so far.

Steps:

1. Initialize `charSet = {}`, `res = 0`, `l = 0`.
2. Iterate with `r` from `0` to `len(s)-1`:
   - While `s[r]` is already in `charSet`:
     - Remove `s[l]` from `charSet`.
     - Increment `l` (shrink window from the left).
   - Add `s[r]` to `charSet`.
   - Update `res = max(res, r - l + 1)`.
3. After loop finishes, `res` is the length of the longest substring without repeating characters.

---

### Walkthrough

Let’s walk through `s = "abcabcbb"`:

| Step | `r` | Character `s[r]` | State before shrinking | Window (`l..r`) | `charSet`             | `res` |
|------|------|------------------|--------------------------|------------------|-------------------------|--------|
| 0    | 0    | 'a'              | ―                        | `a`              | { 'a' }                | 1      |
| 1    | 1    | 'b'              | ―                        | `ab`             | { 'a', 'b' }           | 2      |
| 2    | 2    | 'c'              | ―                        | `abc`            | { 'a', 'b', 'c' }       | 3      |
| 3    | 3    | 'a'              | 'a' is duplicate         | shrink from left until no duplicate → remove 'a' at `l=0` | window becomes `bca` (l=1..3) | { 'b', 'c', 'a' } | 3 |
| 4    | 4    | 'b'              | 'b' duplicate            | remove 'b' at `l=1` → window `cab` | {...} | 3 |
| …    | …    | …                | …                        | …                | …                       | …      |
| Final|      |                  |                          | maximum seen = 3 |                         | 3      |

---

### Complexity Analysis

| Measure      | Complexity |
|---------------|------------|
| Time          | O(n) — each character is added and removed at most once |
| Space         | O(min(n, m)) — where `m` is the size of character set (constant for ASCII, etc.), up to O(n) in worst case |

---

#### [Leetcode Post, Python3](https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/7199314/sliding-window-in-python3-by-milyik-tffc)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l = 0                       #left pointer

        for r in range(len(s)):     #right pointer
            while s[r] in charSet:  #If the new character s[r] is already in the set
                charSet.remove(s[l])
                l += 1              #move left pointer to the right
            charSet.add(s[r])
            res = max(res, r -l + 1)
        return res
```
