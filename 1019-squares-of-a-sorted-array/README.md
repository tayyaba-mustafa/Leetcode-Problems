<h2><a href="https://leetcode.com/problems/squares-of-a-sorted-array">1019. Squares of a Sorted Array</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing</strong> order, return <em>an array of <strong>the squares of each number</strong> sorted in non-decreasing order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-4,-1,0,3,10]
<strong>Output:</strong> [0,1,9,16,100]
<strong>Explanation:</strong> After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-7,-3,2,3,11]
<strong>Output:</strong> [4,9,9,49,121]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code><span>1 &lt;= nums.length &lt;= </span>10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Squaring each element and sorting the new array is very trivial, could you find an <code>O(n)</code> solution using a different approach?

🧠𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵:
This efficient solution leverages the concept of 𝐭𝐰𝐨 𝐩𝐨𝐢𝐧𝐭𝐞𝐫𝐬 to 𝐬𝐨𝐫𝐭 the 𝐬𝐪𝐮𝐚𝐫𝐞𝐬 of the input array in 𝐚𝐬𝐜𝐞𝐧𝐝𝐢𝐧𝐠 𝐨𝐫𝐝𝐞𝐫.

->𝐈𝐧𝐢𝐭𝐢𝐚𝐥𝐢𝐳𝐚𝐭𝐢𝐨𝐧:
Create an empty array 𝐚𝐧𝐬 to store the sorted squares.
Initialize two pointers:
- 𝐥 points to the 𝐛𝐞𝐠𝐢𝐧𝐧𝐢𝐧𝐠 of the array.
- 𝐫 points to the 𝐞𝐧𝐝 of the array.
- 
->𝐈𝐭𝐞𝐫𝐚𝐭𝐢𝐨𝐧:
Iterate from the 𝐞𝐧𝐝 of the array to the 𝐛𝐞𝐠𝐢𝐧𝐧𝐢𝐧𝐠:
Compare the 𝐚𝐛𝐬𝐨𝐥𝐮𝐭𝐞 𝐯𝐚𝐥𝐮𝐞𝐬 of 𝐧𝐮𝐦𝐬[𝐥] and 𝐧𝐮𝐦𝐬[𝐫].
If abs(nums[l]) is greater, it means the square of nums[l] will be larger. Assign the square of nums[l] to the current position in ans and increment l.Otherwise,assign the square of nums[r] to the current position in ans and decrement r.

->𝐑𝐞𝐭𝐮𝐫𝐧:
Return the sorted array 𝐚𝐧𝐬.

🎯𝗧𝗶𝗺𝗲 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(n)
