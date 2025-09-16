---
difficulty: Medium
tags:
    - Hash Table
    - String
    - Sorting
---

<!-- problem:start -->

# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams)

## Description

<!-- description:start -->

<p>Given an array of strings <code>strs</code>, group the anagrams together. You can return the answer in any order.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> strs = ["eat","tea","tan","ate","nat","bat"]
<strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> strs = [""]
<strong>Output:</strong> [[""]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> strs = ["a"]
<strong>Output:</strong> [["a"]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>

<!-- description:end -->

## Solutions

<!-- solution:start -->

### Solution → Character Count as Key

The key idea is that **anagrams share the same character frequency**.  
We can map each string to a 26-length count array representing the frequency of each letter.  
Strings with the same counts belong to the same group.

---

### Walkthrough

Take input: `["eat","tea","tan","ate","nat","bat"]`

| String | Count Array (a→z)      | Key (tuple)                 | Group Updates          |
|--------|------------------------|-----------------------------|------------------------|
| "eat"  | [1,0,0,0,1,0,...,1,...]| (1,0,0,0,1,0,...,1,...)     | {"key1": ["eat"]}      |
| "tea"  | same as "eat"          | same                        | {"key1": ["eat","tea"]}|
| "tan"  | [1,0,0,0,0,0,...,1,...]| new key                     | {"key2": ["tan"]}      |
| "ate"  | same as "eat"          | same                        | {"key1": ["eat","tea","ate"]}|
| "nat"  | same as "tan"          | same                        | {"key2": ["tan","nat"]}|
| "bat"  | [1,1,0,...,1,...]      | new key                     | {"key3": ["bat"]}      |

Final result: `[["eat","tea","ate"], ["tan","nat"], ["bat"]]`

---

### Complexity Analysis

- **Time Complexity:**  
  For each string of length `k`, we count characters in `O(k)`.  
  With `n` strings → **O(n * k)**.

- **Space Complexity:**  
  - Dictionary holds up to `n` keys.  
  - Each key is a tuple of length 26 → `O(1)` space per key.  
  - Total storage of all strings → **O(n * k)**.

---

### Python3

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # mapping from char counts → list of anagrams

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())
