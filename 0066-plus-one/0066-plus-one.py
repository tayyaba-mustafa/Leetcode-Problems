class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr=[]
        x = ''.join(map(str,digits))
        num = int(x) + 1
        while num>0:
            arr.append(num%10)
            num//=10
        arr.reverse()
        return arr

        