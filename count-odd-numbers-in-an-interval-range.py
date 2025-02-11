class Solution:
    def countOdds(self, low: int, high: int) -> int:

        diff = high - low

        if diff%2 == 0:
            if high%2 == 0 and low%2 == 0:
                return int((high-low)/2)
            else:
                return int((high-low)/2 + 1)
        else:
            return int((high-low)//2 + 1)


solObj = Solution()

print(solObj.countOdds(8,10))