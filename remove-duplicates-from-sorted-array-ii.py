from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=2
        l = len(nums)
        if l < 3:
            return l
        for i in range(2,l,1):
            if nums[i] != nums[j-2]:
                nums[j]= nums[i]
                j+=1
        return j

nums = [1,1,1,1,1,1,1]

solObj = Solution()


print(nums[0:solObj.removeDuplicates(nums)])