# Given an integer array nums and an integer k,
# return true if there are two distinct indices i and j in
# the array such that nums[i] == nums[j] and abs(i - j) <= k.

from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    ref_dict = {}
    for i in range(len(nums)):
        if nums[i] not in ref_dict or abs(i - ref_dict[nums[i]]) > k :
            ref_dict[nums[i]] = i
        else:
            return True
    return False

nums = [1,2,3,1]
k = 3
assert containsNearbyDuplicate(nums, k) == True

nums = [1,0,1,1]
k = 1
assert containsNearbyDuplicate(nums, k) == True

nums = [1,2,3,1,2,3]
k = 2
assert containsNearbyDuplicate(nums, k) == False
