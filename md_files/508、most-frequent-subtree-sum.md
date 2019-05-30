---
title: leetcode : 出现次数最多的子树元素和
date: 2019-05-29 11:33:05
tags: [Python3, Leetcode]
---

[出现次数最多的子树元素和](https://leetcode-cn.com/problems/most-frequent-subtree-sum/)

<p>给出二叉树的根，找出出现次数最多的子树元素和。一个结点的子树元素和定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。然后求出出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的元素（不限顺序）。</p>

<!-- more -->

<p>&nbsp;</p>

<p><strong>示例 1</strong><br>
输入:</p>

<pre>  5
 /  \
2   -3
</pre>

<p>返回&nbsp;[2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。</p>

<p><strong>示例&nbsp;2</strong><br>
输入:</p>

<pre>  5
 /  \
2   -5
</pre>

<p>返回&nbsp;[2]，只有 2 出现两次，-5 只出现 1 次。</p>

<p>&nbsp;</p>

<p><strong>提示：</strong>&nbsp;假设任意子树元素和均可以用 32 位有符号整数表示。</p>
