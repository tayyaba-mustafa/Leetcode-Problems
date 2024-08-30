class Solution {
public:
    bool isPalindrome(int x) {
     int temp=x;
     int reverseNum=0;
     if(x<0){return false;}
while(x!=0)
    {
	    int lastdigit=x%10;
        if((reverseNum>INT_MAX/10) || (reverseNum<INT_MIN/10)){
            return 0;}
		x=x/10;
		reverseNum=reverseNum*10+lastdigit;  
    }
if(temp==reverseNum){return true;}
else{return false;}
    }
};