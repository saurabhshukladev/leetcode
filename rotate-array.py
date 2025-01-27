from typing import List

class Solution:
    def reverse(self,nums: List[int],l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1


    def rotate(self, nums: List[int], k: int) -> None:
        size = len(nums) - 1
        k = k%size
        self.reverse(nums,0,size)
        self.reverse(nums,0,k -1)
        self.reverse(nums,size - k,size)




# # Method 1
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         size = len(nums)
#         index = k%size
#         back = nums[size - index:size]
#         front = nums[0:size-index]

#         print(back)
#         print(front)
#         nums.clear()
#         nums.extend(back+front)

nums = [1,2,3,4,5,6,7]
k = 3
solObj = Solution()
solObj.rotate(nums,k)

print(nums)