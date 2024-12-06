class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        def get_next_number(n):
            sum=0
            while n!=0:
                sum += (n%10)**2
                n//=10
            return sum 
        while n not in visit:
            visit.add(n)
            n = get_next_number(n)
            if n== 1:
                return True
        return False
        