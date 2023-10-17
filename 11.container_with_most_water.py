# You are given an integer array height of length n.
# There are n vertical lines drawn such that the
# two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.
from typing import List
def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    water = 0
    while (left != right):
        water = max(abs(min(height[left], height[right]) * (right - left)), water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return water

# height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
height = [2,3,4,5,18,17,6]
print(maxArea(height))
