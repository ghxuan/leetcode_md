---
title: leetcode : 串联所有单词的子串
date: 2019-05-29 11:33:03
tags: [Python3, Leetcode]
---

[串联所有单词的子串](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/)

<p>给定一个字符串&nbsp;<strong>s&nbsp;</strong>和一些长度相同的单词&nbsp;<strong>words。</strong>找出 <strong>s </strong>中恰好可以由&nbsp;<strong>words </strong>中所有单词串联形成的子串的起始位置。</p>

<!-- more -->

<p>注意子串要与&nbsp;<strong>words </strong>中的单词完全匹配，中间不能有其他字符，但不需要考虑&nbsp;<strong>words&nbsp;</strong>中单词串联的顺序。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：
  s =</strong> &quot;barfoothefoobarman&quot;,
<strong>  words = </strong>[&quot;foo&quot;,&quot;bar&quot;]
<strong>输出：</strong><code>[0,9]</code>
<strong>解释：</strong>
从索引 0 和 9 开始的子串分别是 &quot;barfoor&quot; 和 &quot;foobar&quot; 。
输出的顺序不重要, [9,0] 也是有效答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：
  s =</strong> &quot;wordgoodgoodgoodbestword&quot;,
<strong>  words = </strong>[&quot;word&quot;,&quot;good&quot;,&quot;best&quot;,&quot;word&quot;]
<code><span style=""><strong>输出：</strong></span>[]</code>
</pre>
