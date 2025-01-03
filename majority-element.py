from  typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ranking = {}
        for n in nums:
            if(not ranking.__contains__(n)):
                ranking[n] = 1
            else:
                ranking[n] = ranking[n] + 1


        major = 0
        major_key = 0
        
        # TODO merge this loop in the first loop
        for key in ranking.keys(): 
            if major < ranking[key]:
                major = ranking[key]
                major_key = key

        return major_key


sol_obj = Solution()

sol_obj.majorityElement([1,2,2,1,2,2,1])