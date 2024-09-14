<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array">26. Remove Duplicates from Sorted Array</a></h2><h3>Easy</h3><hr><p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a> such that each unique element appears only <strong>once</strong>. The <strong>relative order</strong> of the elements should be kept the <strong>same</strong>. Then return <em>the number of unique elements in </em><code>nums</code>.</p>

<p>Consider the number of unique elements of <code>nums</code> to be <code>k</code>, to get accepted, you need to do the following things:</p>

<ul>
	<li>Change the array <code>nums</code> such that the first <code>k</code> elements of <code>nums</code> contain the unique elements in the order they were present in <code>nums</code> initially. The remaining elements of <code>nums</code> are not important as well as the size of <code>nums</code>.</li>
	<li>Return <code>k</code>.</li>
</ul>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i &lt; k; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong> 2, nums = [1,2,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,1,1,1,2,2,3,3,4]
<strong>Output:</strong> 5, nums = [0,1,2,3,4,_,_,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>

🧠𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵:

->I employed a straightforward approach using 𝐭𝐰𝐨 𝐩𝐨𝐢𝐧𝐭𝐞𝐫𝐬.

->One pointer (𝐢) tracks the 𝐧𝐞𝐱𝐭 𝐚𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 𝐢𝐧𝐝𝐞𝐱, while the other (𝐣) iterates 𝐭𝐡𝐫𝐨𝐮𝐠𝐡 𝐭𝐡𝐞 𝐚𝐫𝐫𝐚𝐲.

->If the current element (𝐧𝐮𝐦𝐬[𝐣]) is 𝐝𝐢𝐟𝐟𝐞𝐫𝐞𝐧𝐭 from the previous element (𝐧𝐮𝐦𝐬[𝐢-𝟏]), it's a 𝐮𝐧𝐢𝐪𝐮𝐞 𝐯𝐚𝐥𝐮𝐞.

->We 𝐜𝐨𝐩𝐲 it to the i-th position and 𝐢𝐧𝐜𝐫𝐞𝐦𝐞𝐧𝐭 i.

->The 𝐟𝐢𝐧𝐚𝐥 𝐯𝐚𝐥𝐮𝐞 of 𝐢 represents the 𝐧𝐞𝐰 𝐥𝐞𝐧𝐠𝐭𝐡 of the array after duplicates are removed.

🎯𝗧𝗶𝗺𝗲 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(n)

🎯𝐒𝐩𝐚𝐜𝐞 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(1)
