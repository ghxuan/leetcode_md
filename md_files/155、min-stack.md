---
title: leetcode : 最小栈
date: 2019-05-29 11:33:04
tags: [Python3, Leetcode]
---

[最小栈](https://leetcode-cn.com/problems/min-stack/)

<p>设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。</p>

<!-- more -->

<ul>
	<li>push(x)&nbsp;-- 将元素 x 推入栈中。</li>
	<li>pop()&nbsp;-- 删除栈顶的元素。</li>
	<li>top()&nbsp;-- 获取栈顶元素。</li>
	<li>getMin() -- 检索栈中的最小元素。</li>
</ul>

<p><strong>示例:</strong></p>

<pre>MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --&gt; 返回 -3.
minStack.pop();
minStack.top();      --&gt; 返回 0.
minStack.getMin();   --&gt; 返回 -2.
</pre>
