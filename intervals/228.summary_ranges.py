from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    r = 0
    len_nums = len(nums)
    res = []
    while (r < len_nums):
        l = r
        while r < len_nums - 1 and nums[r] + 1 == nums[r + 1]:
            r += 1
        if l != r:
            res.append(f'{nums[l]}->{nums[r]}')
        else:
            res.append(f'{nums[r]}')
        r += 1
    return res

nums = [0,1,2,4,5,7]
assert summaryRanges(nums) == ["0->2","4->5","7"]

nums = [0,2,3,4,6,8,9]
assert summaryRanges(nums) == ["0","2->4","6","8->9"]

