<h2><a href="https://leetcode.com/problems/fibonacci-number">1013. Fibonacci Number</a></h2><h3>Easy</h3><hr><p>The <b>Fibonacci numbers</b>, commonly denoted <code>F(n)</code> form a sequence, called the <b>Fibonacci sequence</b>, such that each number is the sum of the two preceding ones, starting from <code>0</code> and <code>1</code>. That is,</p>

<pre>
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n &gt; 1.
</pre>

<p>Given <code>n</code>, calculate <code>F(n)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> F(2) = F(1) + F(0) = 1 + 0 = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 2
<strong>Explanation:</strong> F(3) = F(2) + F(1) = 1 + 1 = 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 3
<strong>Explanation:</strong> F(4) = F(3) + F(2) = 2 + 1 = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 30</code></li>
</ul>

🧠𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵:

This code uses a 𝐫𝐞𝐜𝐮𝐫𝐬𝐢𝐯𝐞 𝐚𝐩𝐩𝐫𝐨𝐚𝐜𝐡 to calculate the 𝐧𝐭𝐡 𝐅𝐢𝐛𝐨𝐧𝐚𝐜𝐜𝐢 𝐧𝐮𝐦𝐛𝐞𝐫. The 𝐟𝐢𝐛 function checks if 𝐧 is 𝐥𝐞𝐬𝐬 𝐭𝐡𝐚𝐧 or 𝐞𝐪𝐮𝐚𝐥 𝐭𝐨 𝟏. If so, it returns 𝐧. Otherwise, it recursively calls itself with 𝐧-𝟏 and 𝐧-𝟐 and adds the results.

🎯𝗧𝗶𝗺𝗲 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(2^n)
