---
title: leetcode : 从英文中重建数字
date: 2019-05-29 11:33:05
tags: [Python3, Leetcode]
---

[从英文中重建数字](https://leetcode-cn.com/problems/reconstruct-original-digits-from-english/)

<p>给定一个<strong>非空</strong>字符串，其中包含字母顺序打乱的英文单词表示的数字<code>0-9</code>。按升序输出原始的数字。</p>

<!-- more -->

<p><strong>注意:</strong></p>

<ol>
	<li>输入只包含小写英文字母。</li>
	<li>输入保证合法并可以转换为原始的数字，这意味着像 &quot;abc&quot; 或 &quot;zerone&quot; 的输入是不允许的。</li>
	<li>输入字符串的长度小于 50,000。</li>
</ol>

<p><strong>示例 1:</strong></p>

<pre>
输入: &quot;owoztneoer&quot;

输出: &quot;012&quot; (zeroonetwo)
</pre>

<p><strong>示例 2:</strong></p>

<pre>
输入: &quot;fviefuro&quot;

输出: &quot;45&quot; (fourfive)
</pre>
