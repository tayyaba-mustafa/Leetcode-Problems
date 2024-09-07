<h2><a href="https://leetcode.com/problems/move-zeroes">283. Move Zeroes</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code>, move all <code>0</code>&#39;s to the end of it while maintaining the relative order of the non-zero elements.</p>

<p><strong>Note</strong> that you must do this in-place without making a copy of the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,0,3,12]
<strong>Output:</strong> [1,3,12,0,0]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you minimize the total number of operations done?

🧠𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵: 

First,we declare a variable 𝐥 and initializes it to 𝟎. This variable will be used as a pointer to keep track of the index where the next non-zero element should be placed. Then we use a 𝐟𝐨𝐫 𝐥𝐨𝐨𝐩 that iterates over each element in the nums list, using the variable 𝐫 as the index. Then we apply 𝐢𝐟 𝐜𝐨𝐧𝐝𝐢𝐭𝐢𝐨𝐧 to check if the current element at index 𝐫 𝐢𝐬 𝐧𝐨𝐭 𝐞𝐪𝐮𝐚𝐥 𝐭𝐨 𝟎. If the condition is 𝐭𝐫𝐮𝐞 (i.e., the current element is not 0), then 𝐬𝐰𝐚𝐩𝐬 the elements at indices 𝐥 and 𝐫. This effectively moves the non-zero element to the beginning of the list. After swapping the elements,𝐢𝐧𝐜𝐫𝐞𝐦𝐞𝐧𝐭𝐬 the 𝐥 𝐩𝐨𝐢𝐧𝐭𝐞𝐫 by 𝟏. When the loop ends,return nums. This effectively moves all zeros to the end of the list.

🎯𝗧𝗶𝗺𝗲 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(n)
