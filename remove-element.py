def removeElement(nums: list[int], val: int) -> int:
    
    count = 0
    for n in range(len(nums)):
        if nums[n] == val:
            nums[n] = 51
            count += 1
    newNums = sorted(nums)
    nums.clear()
    nums.extend(sorted(newNums))
    print(nums)
    print(count)
    return len(nums) - count

nums = [0,1,2,2,3,0,4,2]

# removeElement(nums, 2)





# # method from solutions
# def removeElementSolution(nums: list[int], val: int) -> int:

#     index = 0

#     for i in range(len(nums)):

#         if nums[i] != val:

#             nums[index] = nums[i]

#             index += 1

#     return index




# removeElementSolution(nums,2)
# print(nums)