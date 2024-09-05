class Solution {
public:
    int reverse(int x) {
    int reverseNum=0;
while(x!=0)
    {
	    int lastdigit=x%10;
	    int lastdigit=x%10;
        if((reverseNum>INT_MAX/10) || (reverseNum<INT_MIN/10)){
            return 0;
        }
		x=x/10;
		reverseNum=reverseNum*10+lastdigit;  
    }    
    return reverseNum;
  }
};
