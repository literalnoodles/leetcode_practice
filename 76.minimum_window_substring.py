# Given two strings s and t of lengths m and n respectively, return the minimum window substring
# of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".
# The testcases will be generated such that the answer is unique.

def minWindow(s: str, t: str) -> str:
    ref_dict = {}
    for c in t:
        ref_dict[c] = ref_dict.get(c, 0) + 1
    total_found = 0
    len_t = len(t)
    r = 0
    l = 0
    compare_dict = {}
    result = ''
    while r < len(s):
        if (s[r] in ref_dict):
            compare_dict[s[r]] = compare_dict.get(s[r], 0) + 1
            if (compare_dict[s[r]] <= ref_dict[s[r]]):
                total_found += 1
            # if found, update r value
            if (total_found == len_t):
                while l < r:
                    if s[l] not in ref_dict:
                        l += 1
                    elif compare_dict[s[l]] > ref_dict[s[l]]:
                        compare_dict[s[l]] -= 1
                        l += 1
                    else:
                        break
                if not result or len(result) > r-l+1:
                    result = s[l:r+1]
        r += 1
    return result

s = "ADOBECODEBANC"
t = "ABC"
assert minWindow(s, t) == "BANC"

s = "a"
t = "a"
assert minWindow(s, t) == "a"

s = "a"
t = "aa"
assert minWindow(s, t) == ""