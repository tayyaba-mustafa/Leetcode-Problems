<h2><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii">122. Best Time to Buy and Sell Stock II</a></h2><h3>Medium</h3><hr><p>You are given an integer array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>On each day, you may decide to buy and/or sell the stock. You can only hold <strong>at most one</strong> share of the stock at any time. However, you can buy it then immediately sell it on the <strong>same day</strong>.</p>

<p>Find and return <em>the <strong>maximum</strong> profit you can achieve</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> prices = [1,2,3,4,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>

🧠𝗔𝗽𝗽𝗿𝗼𝗮𝗰𝗵:

This approach involves 𝐢𝐭𝐞𝐫𝐚𝐭𝐢𝐧𝐠 over the prices array and 𝐬𝐮𝐦𝐦𝐢𝐧𝐠 𝐮𝐩 the 𝐩𝐨𝐬𝐢𝐭𝐢𝐯𝐞 𝐝𝐢𝐟𝐟𝐞𝐫𝐞𝐧𝐜𝐞𝐬 between consecutive days.This means buying on one day and 𝐬𝐞𝐥𝐥𝐢𝐧𝐠 on the next day whenever the 𝐩𝐫𝐢𝐜𝐞 𝐢𝐬 𝐡𝐢𝐠𝐡𝐞𝐫 on the next day.

First we declare a variable 𝐦𝐚𝐱𝐩𝐫𝐨𝐟𝐢𝐭 and initialize it to 𝟎. Then apply a 𝐟𝐨𝐫 𝐥𝐨𝐨𝐩.The loop iterates over the price array, starting from the second element. If the 𝐜𝐮𝐫𝐫𝐞𝐧𝐭 𝐩𝐫𝐢𝐜𝐞 is 𝐡𝐢𝐠𝐡𝐞𝐫 than the 𝐩𝐫𝐞𝐯𝐢𝐨𝐮𝐬 𝐩𝐫𝐢𝐜𝐞, the difference is added to maxprofit. Then return maxprofit.

𝐆𝐫𝐞𝐞𝐝𝐲 𝐀𝐩𝐩𝐫𝐨𝐚𝐜𝐡: This solution adopts a greedy strategy by maximizing the profit at each step.

🎯𝗧𝗶𝗺𝗲 𝗖𝗼𝗺𝗽𝗹𝗲𝘅𝗶𝘁𝘆: O(n)
