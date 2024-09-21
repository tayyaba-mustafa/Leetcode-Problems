<h2><a href="https://leetcode.com/problems/minimum-moves-to-equal-array-elements/">453. Minimum Moves to Equal Array Elements</a></h2><h3>Medium</h3><hr><p>Given an integer array <code>nums</code> of size <code>n</code>, return <em>the minimum number of moves required to make all array elements equal</em>.</p>

<p>In one move, you can increment <code>n - 1</code> elements of the array by <code>1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 3
<strong>Explanation:</strong> Only three moves are needed (remember each move increments two elements):
[1,2,3]  =&gt;  [2,3,3]  =&gt;  [3,4,3]  =&gt;  [4,4,4]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>The answer is guaranteed to fit in a <strong>32-bit</strong> integer.</li>
</ul>

🧠𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵:

->In this problem,mathematical approach is used.

->Take the length of the array.

->Now take the sum of all elements of the array.

->Take the minimum value of the array.

->Now Just 𝐦𝐮𝐥𝐭𝐢𝐩𝐥𝐲 the 𝐥𝐞𝐧(𝐧𝐮𝐦𝐬) and 𝐦𝐢𝐧𝐢𝐦𝐮𝐦 𝐯𝐚𝐥𝐮𝐞 of the array.

->𝐒𝐮𝐛𝐭𝐫𝐚𝐜𝐭 the multiplication result from the whole 𝐬𝐮𝐦.


🎯𝗧𝗶𝗺𝗲 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(n)

🎯𝐒𝐩𝐚𝐜𝐞 𝐂𝐨𝐦𝐩𝐥𝐞𝐱𝐢𝐭𝐲: O(1)
