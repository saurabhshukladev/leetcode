from  typing import List

# #Method 1 
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
        
        
#         size = len(nums)

#         if(size == 1):
#             return nums[0]
        

#         ranking = {}
#         for n in nums:
#             if(not ranking.__contains__(n)):
#                 ranking[n] = 1
#             else:
#                 ranking[n] = ranking[n] + 1
#                 if(ranking[n]>size/2):
#                     return n


#         major = 0
#         major_key = 0
        
#         # FIX merge this loop in the first loop
#         for key in ranking.keys(): 
#             if major < ranking[key]:
#                 major = ranking[key]
#                 major_key = key

#         return major_key

#         # https://youtu.be/7pnhv842keE?t=410

# #Method 2: remove second loop
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = {}
#         res,maxCount = None,0

#         for num in nums:
#             count[num] = 1 + count.get(num,0) # dict.get(key, defualt value if no key is found)
#             if count[num] > maxCount:
#                 res, maxCount = num, count[num]

#         return res

# Method 3: Boyer-Moore Majority Voting Algorithm (https://youtu.be/7pnhv842keE?t=410)
class Solution:
    def majorityElement(self,nums: List[int]) -> List[int]:
        count = 0
        max = None

        for num in nums:
            if count == 0:
                max = num
            if num == max:
                count += 1
            else:
                count -= 1
        return max



sol_obj = Solution()

sol_obj.majorityElement([1,2,2,1,2,2,1])