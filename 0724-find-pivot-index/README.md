<h2><a href="https://leetcode.com/problems/find-pivot-index">724. Find Pivot Index</a></h2><h3>Easy</h3><hr><p>Given an array of integers <code>nums</code>, calculate the <strong>pivot index</strong> of this array.</p>

<p>The <strong>pivot index</strong> is the index where the sum of all the numbers <strong>strictly</strong> to the left of the index is equal to the sum of all the numbers <strong>strictly</strong> to the index&#39;s right.</p>

<p>If the index is on the left edge of the array, then the left sum is <code>0</code> because there are no elements to the left. This also applies to the right edge of the array.</p>

<p>Return <em>the <strong>leftmost pivot index</strong></em>. If no such index exists, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,7,3,6,5,6]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
There is no index that satisfies the conditions in the problem statement.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,-1]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as&nbsp;1991:&nbsp;<a href="https://leetcode.com/problems/find-the-middle-index-in-array/" target="_blank">https://leetcode.com/problems/find-the-middle-index-in-array/</a></p>

🧠𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵:

->A 𝐩𝐢𝐯𝐨𝐭 𝐢𝐧𝐝𝐞𝐱 is a position where the 𝐬𝐮𝐦 of elements to its 𝐥𝐞𝐟𝐭 equals the 𝐬𝐮𝐦 of elements to its 𝐫𝐢𝐠𝐡𝐭.

->In this approach,𝐥𝐞𝐟𝐭_𝐬𝐮𝐦 and 𝐫𝐢𝐠𝐡𝐭_𝐬𝐮𝐦 should be the 𝐬𝐚𝐦𝐞.

->𝐂𝐚𝐥𝐜𝐮𝐥𝐚𝐭𝐞 𝐭𝐨𝐭𝐚𝐥 𝐬𝐮𝐦: We first compute the total sum of all elements in the array.

->𝐈𝐭𝐞𝐫𝐚𝐭𝐞 𝐚𝐧𝐝 𝐂𝐨𝐦𝐩𝐚𝐫𝐞: We iterate through the array, keeping track of the left sum. For each element, we calculate the right sum by subtracting the left sum and the current element from the total sum. If the left sum equals the right sum, we've found the pivot index.

->𝐔𝐩𝐝𝐚𝐭𝐞 𝐋𝐞𝐟𝐭 𝐒𝐮𝐦: After checking for the pivot, we update the left sum to include the current element for the next iteration.

🎯𝗧𝗶𝗺𝗲 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(n)
