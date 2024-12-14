class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT32_MIN = -2**31
        INT32_MAX =  2**31 - 1
        d=abs(dividend)
        dv=abs(divisor)
        output=0
        while(d>=dv):
            temp=dv
            mul=1
            while(d>=temp):
                d-=temp
                output+=mul
                mul+=mul
                temp+=temp
        if(dividend<0 and divisor>=0)or(dividend>=0 and divisor<0):
            output=-output
        return min(INT32_MAX,max(INT32_MIN,output))