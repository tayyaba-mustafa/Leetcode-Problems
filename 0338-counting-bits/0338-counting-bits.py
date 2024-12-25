class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[]
        if n==0: return [0]   
        if n==1: return [0,1]
        def get_ones_in_number(n): 
            count=0   
            for i in range(20,-1,-1):
                if (n>=(2**i)):
                    n=n-(2**i)
                    count+=1
                    if (n==0):  break   
            return count 
        for i in range(0,n+1):
            arr.append(get_ones_in_number(i))
        return arr
        