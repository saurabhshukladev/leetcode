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

removeElement(nums, 2)






