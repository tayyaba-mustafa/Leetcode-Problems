<h2><a href="https://leetcode.com/problems/reverse-integer">7. Reverse Integer</a></h2><h3>Medium</h3><hr><p>Given a signed 32-bit integer <code>x</code>, return <code>x</code><em> with its digits reversed</em>. If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>

<p><strong>Assume the environment does not allow you to store 64-bit integers (signed or unsigned).</strong></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 123
<strong>Output:</strong> 321
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = -123
<strong>Output:</strong> -321
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 120
<strong>Output:</strong> 21
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

🧠𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵: 
Create a variable reverseNum and initialize it to 0. This variable will hold the reversed number.Use a while loop to iterate as long as x is not zero.Extract the last digit of x using x % 10 and store it in the variable lastdigit.Check if appending the lastdigit to reverseNum would cause overflow or underflow. This is done by comparing reverseNum with INT_MAX / 10 and INT_MIN / 10.If the overflow or underflow condition is detected, return 0.Remove the last digit from x by performing x/10.
Update reverseNum by multiplying it by 10 and adding the lastdigit.After the loop ends,return reverseNum.

🎯𝗧𝗶𝗺𝗲 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(logn)
