class Solution:
    def countOdds(self, low: int, high: int) -> int:

        count = 0;
        for i in range(low,high):
            if i%2 == 0:
                  count + = 1          
        
        return 5


solObj = Solution()

print(solObj.countOdds(3,7))