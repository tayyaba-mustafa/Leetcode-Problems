class Solution:
    def getSum(self, a: int, b: int) -> int:
        c=abs(a)
        d=abs(b)
        if(a>=0 and b>=0):
            for i in range(d):
                c=c+1 
            return c    
        if( a<0 and b < 0):
            for i in range(d):
                c=c+1         
            return -c              
        if(a>=0 and b<=0 or a<=0 and b>=0):
            for i in range(d):
                c=c-1  
        if(a>=0 and b<=0):    
            return c
        if(a<=0 and b>=0):
            return -c     
        