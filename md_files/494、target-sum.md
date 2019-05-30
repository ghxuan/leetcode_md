---
title: leetcode : 目标和
date: 2019-05-29 11:33:05
tags: [Python3, Leetcode]
---

[目标和](https://leetcode-cn.com/problems/target-sum/)

<p>给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号&nbsp;<code>+</code>&nbsp;和&nbsp;<code>-</code>。对于数组中的任意一个整数，你都可以从&nbsp;<code>+</code>&nbsp;或&nbsp;<code>-</code>中选择一个符号添加在前面。</p>

<!-- more -->

<p>返回可以使最终数组和为目标数 S 的所有添加符号的方法数。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums: [1, 1, 1, 1, 1], S: 3
<strong>输出:</strong> 5
<strong>解释:</strong> 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>数组的长度不会超过20，并且数组中的值全为正数。</li>
	<li>初始的数组的和不会超过1000。</li>
	<li>保证返回的最终结果为32位整数。</li>
</ol>
