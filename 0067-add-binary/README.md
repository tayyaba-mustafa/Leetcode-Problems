<h2><a href="https://leetcode.com/problems/add-binary">67. Add Binary</a></h2><h3>Easy</h3><hr><p>Given two binary strings <code>a</code> and <code>b</code>, return <em>their sum as a binary string</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> a = "11", b = "1"
<strong>Output:</strong> "100"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> a = "1010", b = "1011"
<strong>Output:</strong> "10101"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length &lt;= 10<sup>4</sup></code></li>
	<li><code>a</code> and <code>b</code> consist&nbsp;only of <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code> characters.</li>
	<li>Each string does not contain leading zeros except for the zero itself.</li>
</ul>

🧠𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵:

In this approach,Python built-in functions are used for a simpler and efficient solution.

𝐂𝐨𝐧𝐯𝐞𝐫𝐭 𝐭𝐨 𝐈𝐧𝐭𝐞𝐠𝐞𝐫𝐬: Convert the binary strings a and b to integers using 𝐛𝐚𝐬𝐞 𝟐.

𝐀𝐝𝐝 𝐈𝐧𝐭𝐞𝐠𝐞𝐫𝐬: Add the converted integers to get the sum.

𝐂𝐨𝐧𝐯𝐞𝐫𝐭 𝐭𝐨 𝐁𝐢𝐧𝐚𝐫𝐲: Convert the 𝐬𝐮𝐦 back to a 𝐛𝐢𝐧𝐚𝐫𝐲 𝐬𝐭𝐫𝐢𝐧𝐠 and return the result, excluding the leading '𝟎𝐛' prefix.

🎯𝗧𝗶𝗺𝗲 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(max(m, n))
