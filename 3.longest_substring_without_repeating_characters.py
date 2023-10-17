# Given a string s, find the length of the longest
# substring
# without repeating characters.

def lengthOfLongestSubstring(s: str) -> int:
    longest = 0
    visited = {}
    left, right = 0, 0
    while right < len(s):
        if visited.get(s[right]) is not None and visited.get(s[right]) >= left:
            left = visited.get(s[right]) + 1
        else:
            longest = max(longest, right - left + 1)
        visited[s[right]] = right
        right += 1
    return longest

s = "pwwkew"
s = "abcabcbb"
# s = "bbbbb"
# s = ""
# s = " "
# s = "au"
print(lengthOfLongestSubstring(s))

