def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """


    res = []

    if n == 0:
        
        res[:] =  nums1
    elif m == 0:
        
        res[:] =  nums2
    else:
        mi = 0
        ni = 0

        for i in range(m + n):
            if mi < m and ni < n:
                if nums1[mi] < nums2[ni]:
                    res.append(nums1[mi])
                    mi = mi + 1
                else:
                    res.append(nums2[ni])
                    ni = ni + 1
            elif mi < m:
                res.append(nums1[mi])
                mi = mi + 1
            elif ni < n:
                res.append(nums2[ni])
                ni = ni + 1


    nums1[:] = res

    return nums1


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
