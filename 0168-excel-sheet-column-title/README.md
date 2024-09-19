<h2><a href="https://leetcode.com/problems/excel-sheet-column-title">168. Excel Sheet Column Title</a></h2><h3>Easy</h3><hr><p>Given an integer <code>columnNumber</code>, return <em>its corresponding column title as it appears in an Excel sheet</em>.</p>

<p>For example:</p>

<pre>
A -&gt; 1
B -&gt; 2
C -&gt; 3
...
Z -&gt; 26
AA -&gt; 27
AB -&gt; 28 
...
</pre>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> columnNumber = 1
<strong>Output:</strong> &quot;A&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> columnNumber = 28
<strong>Output:</strong> &quot;AB&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> columnNumber = 701
<strong>Output:</strong> &quot;ZY&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= columnNumber &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

🧠𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵:

->Initialize an empty string 𝐚𝐧𝐬 to store the result.

->While the 𝐜𝐨𝐥𝐮𝐦𝐧𝐍𝐮𝐦𝐛𝐞𝐫 is greater than 0:

->Calculate the 𝐢𝐧𝐝𝐞𝐱 of the current character by taking the remainder of columnNumber - 1 divided by 26.

->Append the character corresponding to the calculated index (using ASCII values) to the beginning of ans.

->Update columnNumber by dividing it by 26 and flooring the result.

->Return the final ans string.

🎯𝗧𝗶𝗺𝗲 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(log(columnNumber))
