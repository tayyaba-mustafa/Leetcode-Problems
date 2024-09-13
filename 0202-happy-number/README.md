<h2><a href="https://leetcode.com/problems/happy-number">202. Happy Number</a></h2><h3>Easy</h3><hr><p>Write an algorithm to determine if a number <code>n</code> is happy.</p>

<p>A <strong>happy number</strong> is a number defined by the following process:</p>

<ul>
	<li>Starting with any positive integer, replace the number by the sum of the squares of its digits.</li>
	<li>Repeat the process until the number equals 1 (where it will stay), or it <strong>loops endlessly in a cycle</strong> which does not include 1.</li>
	<li>Those numbers for which this process <strong>ends in 1</strong> are happy.</li>
</ul>

<p>Return <code>true</code> <em>if</em> <code>n</code> <em>is a happy number, and</em> <code>false</code> <em>if not</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 19
<strong>Output:</strong> true
<strong>Explanation:</strong>
1<sup>2</sup> + 9<sup>2</sup> = 82
8<sup>2</sup> + 2<sup>2</sup> = 68
6<sup>2</sup> + 8<sup>2</sup> = 100
1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

🧠𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵:

In this approach,we use a 𝐬𝐞𝐭 to keep track of 𝐧𝐮𝐦𝐛𝐞𝐫𝐬 𝐞𝐧𝐜𝐨𝐮𝐧𝐭𝐞𝐫𝐞𝐝 during the calculation. If a number is encountered again, it means we're in a 𝐜𝐲𝐜𝐥𝐞 and the number is not happy.

->First,Create an 𝐞𝐦𝐩𝐭𝐲 𝐬𝐞𝐭 named 𝐬. This set will be used to store the numbers encountered during the calculation process, preventing infinite loops.

->Define a function 𝐧𝐞𝐱𝐭_𝐧𝐮𝐦𝐛𝐞𝐫 to calculates the next number in the happy number sequence.The 𝐧 𝐩𝐚𝐫𝐚𝐦𝐞𝐭𝐞𝐫 represents the 𝐜𝐮𝐫𝐫𝐞𝐧𝐭 𝐧𝐮𝐦𝐛𝐞𝐫.

->Initialize a variable named 𝐬𝐮𝐦 to 𝟎. This variable will accumulate the sum of the squares of the digits of n.

->Start a 𝐰𝐡𝐢𝐥𝐞 𝐥𝐨𝐨𝐩 that continues as long as n is not zero.

->Then extract the 𝐥𝐚𝐬𝐭 𝐝𝐢𝐠𝐢𝐭 of n and stores it in the 𝐝𝐢𝐠𝐢𝐭 variable and add it to the sum.

->Remove the last digit from n by integer dividing it by 10.

->Return the calculated sum, which is the next number in the sequence.

->Use another 𝐰𝐡𝐢𝐥𝐞 𝐥𝐨𝐨𝐩 that continues as long as n is not already present in the s set.

->Add n to the s set to prevent infinite loops.

->Then calculate the 𝐧𝐞𝐱𝐭 𝐧𝐮𝐦𝐛𝐞𝐫 in the sequence using the next_number  function and update n with the result.

->If the current 𝐧 is equal to 𝟏, it means the number is 𝐡𝐚𝐩𝐩𝐲 and return 𝐓𝐫𝐮𝐞.

->If the loop completes without finding n to be equal to 1, it means the number is not happy. So, the function returns 𝐅𝐚𝐥𝐬𝐞.

🎯𝗧𝗶𝗺𝗲 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(logn)
