class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
    int n=nums.size() , count=0;
    vector<int> freq(101,0);
    for(int i=0;i<n;i++){
	    freq[nums[i]]++;
    }

    for(int i=1;i<=100;i++){
	    count=count + (freq[i]-1)*freq[i]/2;
    }
    return count;
    }
};