# Given an unsorted array of integers nums,
# return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    pass

nums = [100,4,200,1,3,2]
assert longestConsecutive(nums) == 4


nums = [0,3,7,2,5,8,4,6,0,1]
assert longestConsecutive(nums) == 9
