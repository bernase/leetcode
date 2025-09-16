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

### Why `defaultdict(list)`?

- Normally, when using a Python dictionary, you must check if a key already exists before appending:
  ```python
  if key in res:
      res[key].append(s)
  else:
      res[key] = [s]
