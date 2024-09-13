class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        def next_number(n):
            sum = 0
            while n:
                digit = n % 10
                sum += digit**2
                n = n//10
            
            return sum
        
        while n not in s:
            s.add(n)
            n = next_number(n)
            if n == 1:
                return True
        
        return False
            
        