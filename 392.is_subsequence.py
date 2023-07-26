# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by
# deleting some (can be none) of the characters without disturbing the relative positions
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

def isSubsequence(s: str, t: str) -> bool:
    l,r = 0, 0
    while l < len(s) and r < len(t):
        while t[r] != s[l]:
            r += 1
            if r >= len(t):
                return False
        l += 1
        r += 1
    if l == len(s):
        return True

    return False
        


s = "abc"
t = "ahbgdc"

s = "axc"
t = "ahbgdc"

print(isSubsequence(s, t))