---
title: leetcode : 把二叉搜索树转换为累加树
date: 2019-05-29 11:33:05
tags: [Python3, Leetcode]
---

[把二叉搜索树转换为累加树](https://leetcode-cn.com/problems/convert-bst-to-greater-tree/)

<p>给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。</p>

<!-- more -->

<p><strong>例如：</strong></p>

<pre>
<strong>输入:</strong> 二叉搜索树:
              5
            /   \
           2     13

<strong>输出:</strong> 转换为累加树:
             18
            /   \
          20     13
</pre>
