---
title: leetcode : 删列造序
date: 2019-05-29 11:33:07
tags: [Python3, Leetcode]
---

[删列造序](https://leetcode-cn.com/problems/delete-columns-to-make-sorted/)

<p>给定由&nbsp;<code>N</code>&nbsp;个小写字母字符串组成的数组 <code>A</code>，其中每个字符串长度相等。</p>

<!-- more -->

<p>选取一个删除索引序列，对于 <code>A</code> 中的每个字符串，删除对应每个索引处的字符。 所余下的字符串行从上往下读形成列。</p>

<p>比如，有&nbsp;<code>A = [&quot;abcdef&quot;, &quot;uvwxyz&quot;]</code>，删除索引序列&nbsp;<code>{0, 2, 3}</code>，删除后 <code>A</code>&nbsp;为<code>[&quot;bef&quot;, &quot;vyz&quot;]</code>， <code>A</code>&nbsp;的列分别为<code>[&quot;b&quot;,&quot;v&quot;], [&quot;e&quot;,&quot;y&quot;], [&quot;f&quot;,&quot;z&quot;]</code>。（形式上，第 n&nbsp;列为&nbsp;<code>[A[0][n], A[1][n], ..., A[A.length-1][n]]</code>）。</p>

<p>假设，我们选择了一组删除索引&nbsp;<code>D</code>，那么在执行删除操作之后，<code>A</code> 中所剩余的每一列都必须是 <strong>非降序</strong>&nbsp;排列的，然后请你返回&nbsp;<code>D.length</code>&nbsp;的最小可能值。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[&quot;cba&quot;, &quot;daf&quot;, &quot;ghi&quot;]
<strong>输出：</strong>1
<strong>解释：</strong>
当选择 D = {1}，删除后 A 的列为：[&quot;c&quot;,&quot;d&quot;,&quot;g&quot;] 和 [&quot;a&quot;,&quot;f&quot;,&quot;i&quot;]，均为非降序排列。
若选择 D = {}，那么 A 的列 [&quot;b&quot;,&quot;a&quot;,&quot;h&quot;] 就不是非降序排列了。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[&quot;a&quot;, &quot;b&quot;]
<strong>输出：</strong>0
<strong>解释：</strong>D = {}
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[&quot;zyx&quot;, &quot;wvu&quot;, &quot;tsr&quot;]
<strong>输出：</strong>3
<strong>解释：</strong>D = {0, 1, 2}
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 100</code></li>
	<li><code>1 &lt;= A[i].length &lt;= 1000</code></li>
</ol>
