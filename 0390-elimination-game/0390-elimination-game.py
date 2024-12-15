class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True
        head = 1
        step = 1 # Difference between consecutive elements
        while n>1:
            if left or n&1:  # Proceed if going left-to-right or if n is odd
                head += step
            step *= 2  # Double the step size
            n //= 2    # Reduce the remaining elements by half
            left = not left  # Toggle the direction
        return head