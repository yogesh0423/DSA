class Solution:
    def pascalTriangleI(self, r: int, c: int) -> int:
        n = r - 1
        k = c - 1
        ans = 1
        for i in range(k):
            ans = ans * (n - i)
            ans = ans / (i + 1)
        return ans