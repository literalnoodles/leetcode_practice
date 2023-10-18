# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    ref_dict = {}
    for i in range(len(nums)):
        search = target - nums[i]
        if ref_dict.get(search) is not None:
            return [ref_dict[search], i]
        else:
            ref_dict[nums[i]] = i

nums = [2,7,11,15]
target = 9
twoSum(nums, target)
# [0,1]

nums = [3,2,4]
target = 6
twoSum(nums, target)
# [1,2]

nums = [3,3]
target = 6
twoSum(nums, target)
# [0,1]