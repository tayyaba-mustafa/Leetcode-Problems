<h2><a href="https://leetcode.com/problems/power-of-two">231. Power of Two</a></h2><h3>Easy</h3><hr><p>Given an integer <code>n</code>, return <em><code>true</code> if it is a power of two. Otherwise, return <code>false</code></em>.</p>

<p>An integer <code>n</code> is a power of two, if there exists an integer <code>x</code> such that <code>n == 2<sup>x</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>0</sup> = 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 16
<strong>Output:</strong> true
<strong>Explanation: </strong>2<sup>4</sup> = 16
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without loops/recursion?

🧠𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵:

-𝐈𝐭𝐞𝐫𝐚𝐭𝐢𝐨𝐧: We iterate through the integers from 𝟎 𝐭𝐨 𝟑𝟎 (assuming a 𝟑𝟐-𝐛𝐢𝐭 integer).

-𝐏𝐨𝐰𝐞𝐫 𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐢𝐨𝐧: In each iteration, we calculate 𝟐 raised to the current exponent (𝐢).

-𝐂𝐨𝐦𝐩𝐚𝐫𝐢𝐬𝐨𝐧: We compare the 𝐜𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐞𝐝 𝐫𝐞𝐬𝐮𝐥𝐭 with the given integer (𝐧). If they match, we return 𝐭𝐫𝐮𝐞 as n is a power of two.

-𝐑𝐞𝐭𝐮𝐫𝐧 𝐅𝐚𝐥𝐬𝐞: If no match is found after iterating through all exponents, we return false.

🎯𝗧𝗶𝗺𝗲 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(logn)

🎯𝐒𝐩𝐚𝐜𝐞 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(1)
