def removeDuplicates2(nums: list[int]) -> int:


# try 2 pointer 1 waits on number to be replaced while other keeps moving    

    i=1
    j=1
    len_num = len(nums)

    while i < len_num:
        if nums[i] != nums[j-1]:
            nums[j] = nums[i]
            j+=1
            
        i+=1

    return j


def removeDuplicates1(nums: list[int]) -> int:
    i = 0
    count = 0
    num_size = len(nums)
    while i < num_size:

        if i> 0 and nums[i-1] >= nums[i]:
            nums[i-1] = 101
            count+=1
        i+=1
        
    nums[:] = sorted(nums)

    return num_size - count

nums =[0,0,1,1,1,2,2,3,3,4]
ans = removeDuplicates2(nums)
print(ans)

print(nums[0:ans])


