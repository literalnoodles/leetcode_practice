# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray 
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    min_len = float('inf')
    l, r = 0, 0
    total = 0
    print(nums)
    while r < len(nums) or total >= target:
        print(f"l: {l}, r: {r}, total: {total}, min: {min_len}")
        if (total < target):
            total += nums[r]
            r += 1
        else:
            total -= nums[l]
            min_len = min(min_len, r - l)
            l += 1
    return min_len


target = 7
nums = [2,3,1,2,4,3] 
# -> 2
print(minSubArrayLen(target, nums))

# target = 4
# nums = [1,4,4]
# # -> 1
# print(minSubArrayLen(target, nums))

# target = 11
# nums = [1,1,1,1,1,1,1,1]
# # -> 0
# print(minSubArrayLen(target, nums))
