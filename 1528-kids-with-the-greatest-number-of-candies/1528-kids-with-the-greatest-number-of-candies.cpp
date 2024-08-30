class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
    int n=candies.size();
    vector<bool> result(n);
    int Greatest;
    Greatest=candies[0];
    for(int i=1;i<n;i++)
    {
	   if(candies[i]>Greatest) 
	       { 
	           Greatest=candies[i];
		   } 
    }
    for(int i=0;i<n;i++)
    {
	   if(candies[i]+extraCandies>=Greatest) 
	       { 
	           result[i]=true;
		   }
	    else 
	       {
	       	   result[i]=false;
		   }
    } 
    return result;
    }
};