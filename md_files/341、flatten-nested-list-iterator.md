---
title: leetcode : 扁平化嵌套列表迭代器
date: 2019-05-29 11:33:04
tags: [Python3, Leetcode]
---

[扁平化嵌套列表迭代器](https://leetcode-cn.com/problems/flatten-nested-list-iterator/)

<p>给定一个嵌套的整型列表。设计一个迭代器，使其能够遍历这个整型列表中的所有整数。</p>

<!-- more -->

<p>列表中的项或者为一个整数，或者是另一个列表。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入: </strong>[[1,1],2,[1,1]]
<strong>输出: </strong>[1,1,2,1,1]
<strong>解释: </strong>通过重复调用&nbsp;<em>next </em>直到&nbsp;<em>hasNex</em>t 返回false，<em>next&nbsp;</em>返回的元素的顺序应该是: <code>[1,1,2,1,1]</code>。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong>[1,[4,[6]]]
<strong>输出: </strong>[1,4,6]
<strong>解释: </strong>通过重复调用&nbsp;<em>next&nbsp;</em>直到&nbsp;<em>hasNex</em>t 返回false，<em>next&nbsp;</em>返回的元素的顺序应该是: <code>[1,4,6]</code>。
</pre>
