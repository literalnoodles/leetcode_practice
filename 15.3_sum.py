# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    # sort the list first
    nums.sort()
    i = 0
    result = []
    while i < len(nums):
        # we find 2 number starting from i+1 to len(nums) - 1
        # with sum = - nums[i]
        left, right = i + 1, len(nums) - 1
        target = - nums[i]
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                # move left so we have new number
                while left+1 < right and nums[left] == nums[left + 1]:
                    left += 1
                left += 1
        # move i
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        i += 1

    return result


nums = [-1,0,1,2,-1,-4]
nums = [0,0,0,0]
# nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
