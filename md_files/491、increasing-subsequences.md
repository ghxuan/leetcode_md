---
title: leetcode : 递增子序列
date: 2019-05-29 11:33:05
tags: [Python3, Leetcode]
---

[递增子序列](https://leetcode-cn.com/problems/increasing-subsequences/)

<p>给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。</p>

<!-- more -->

<p><strong>示例:</strong></p>

<pre>
<strong>输入:</strong> [4, 6, 7, 7]
<strong>输出:</strong> [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>给定数组的长度不会超过15。</li>
	<li>数组中的整数范围是&nbsp;[-100,100]。</li>
	<li>给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。</li>
</ol>
