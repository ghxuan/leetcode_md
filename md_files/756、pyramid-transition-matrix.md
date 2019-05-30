---
title: leetcode : 金字塔转换矩阵
date: 2019-05-29 11:33:06
tags: [Python3, Leetcode]
---

[金字塔转换矩阵](https://leetcode-cn.com/problems/pyramid-transition-matrix/)

<p>现在，我们用一些方块来堆砌一个金字塔。 每个方块用仅包含一个字母的字符串表示，例如 &ldquo;Z&rdquo;。</p>

<!-- more -->

<p>使用三元组表示金字塔的堆砌规则如下：</p>

<p>(A, B, C) 表示，&ldquo;C&rdquo;为顶层方块，方块&ldquo;A&rdquo;、&ldquo;B&rdquo;分别作为方块&ldquo;C&rdquo;下一层的的左、右子块。当且仅当(A, B, C)是被允许的三元组，我们才可以将其堆砌上。</p>

<p>初始时，给定金字塔的基层&nbsp;<code>bottom</code>，用一个字符串表示。一个允许的三元组列表&nbsp;<code>allowed</code>，每个三元组用一个长度为 3 的字符串表示。</p>

<p>如果可以由基层一直堆到塔尖返回true，否则返回false。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> bottom = &quot;XYZ&quot;, allowed = [&quot;XYD&quot;, &quot;YZE&quot;, &quot;DEA&quot;, &quot;FFF&quot;]
<strong>输出:</strong> true
<strong>解析:</strong>
可以堆砌成这样的金字塔:
    A
   / \
  D   E
 / \ / \
X   Y   Z

因为符合(&#39;X&#39;, &#39;Y&#39;, &#39;D&#39;), (&#39;Y&#39;, &#39;Z&#39;, &#39;E&#39;) 和 (&#39;D&#39;, &#39;E&#39;, &#39;A&#39;) 三种规则。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> bottom = &quot;XXYX&quot;, allowed = [&quot;XXX&quot;, &quot;XXY&quot;, &quot;XYX&quot;, &quot;XYY&quot;, &quot;YXZ&quot;]
<strong>输出:</strong> false
<strong>解析:</strong>
无法一直堆到塔尖。
注意, 允许存在三元组(A, B, C)和 (A, B, D) ，其中 C != D.
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li><code>bottom</code> 的长度范围在&nbsp;<code>[2, 8]</code>。</li>
	<li><code>allowed</code> 的长度范围在<code>[0, 200]</code>。</li>
	<li>方块的标记字母范围为<code>{&#39;A&#39;, &#39;B&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;, &#39;F&#39;, &#39;G&#39;}</code>。</li>
</ol>
