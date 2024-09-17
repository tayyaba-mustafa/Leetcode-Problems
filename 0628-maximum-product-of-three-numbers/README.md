<h2><a href="https://leetcode.com/problems/maximum-product-of-three-numbers">628. Maximum Product of Three Numbers</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code>, <em>find three numbers whose product is maximum and return the maximum product</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 6
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> 24
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [-1,-2,-3]
<strong>Output:</strong> -6
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;=&nbsp;10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

🧠𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵:

The goal is to 𝐟𝐢𝐧𝐝 𝐭𝐡𝐞 𝐭𝐡𝐫𝐞𝐞 𝐧𝐮𝐦𝐛𝐞𝐫𝐬 in the array whose 𝐩𝐫𝐨𝐝𝐮𝐜𝐭 is the 𝐥𝐚𝐫𝐠𝐞𝐬𝐭.

->𝐒𝐨𝐫𝐭 𝐭𝐡𝐞 𝐚𝐫𝐫𝐚𝐲: By sorting the array, we can ensure that the largest and smallest numbers are at the ends.

->𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐞 𝐦𝐚𝐱𝐢𝐦𝐮𝐦 𝐩𝐫𝐨𝐝𝐮𝐜𝐭: We consider two cases:

𝐏𝐫𝐨𝐝𝐮𝐜𝐭 𝐨𝐟 𝐭𝐡𝐞 𝐥𝐚𝐫𝐠𝐞𝐬𝐭 𝐭𝐡𝐫𝐞𝐞 𝐧𝐮𝐦𝐛𝐞𝐫𝐬: nums[-1] * nums[-2] * nums[-3]

𝐏𝐫𝐨𝐝𝐮𝐜𝐭 𝐨𝐟 𝐭𝐡𝐞 𝐬𝐦𝐚𝐥𝐥𝐞𝐬𝐭 𝐭𝐰𝐨 𝐧𝐮𝐦𝐛𝐞𝐫𝐬 𝐚𝐧𝐝 𝐭𝐡𝐞 𝐥𝐚𝐫𝐠𝐞𝐬𝐭 𝐧𝐮𝐦𝐛𝐞𝐫: nums[0] * nums[1] * nums[-1]

->Then,return the maximum of these two products.

🎯𝗧𝗶𝗺𝗲 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(nlogn)
