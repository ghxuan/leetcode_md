---
title: leetcode : 打乱数组
date: 2019-05-29 11:33:04
tags: [Python3, Leetcode]
---

[打乱数组](https://leetcode-cn.com/problems/shuffle-an-array/)

<p>打乱一个没有重复元素的数组。</p>

<!-- more -->

<p><strong>示例:</strong></p>

<pre>
// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();
</pre>
