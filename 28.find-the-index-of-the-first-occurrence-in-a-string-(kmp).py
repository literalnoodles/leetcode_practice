def findStr(haystack: str, needle: str):
    i, j = 0, 0
    lps = get_lps(needle)
    while i < len(haystack):
        if haystack[i] == needle[j]:
            if j == len(needle) - 1:
                return i - len(needle) + 1
            else:
                i += 1
                j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]

def get_lps(input_str):
    lps = [0] * len(input_str)
    l, i = 0, 1
    while i < len(input_str):
        if input_str[l] == input_str[i]:
            l += 1
            lps[i] = l
            i += 1
        else:
            if l == 0:
                lps[i] = l
                i += 1
            else:
                l = lps[l-1]
    return lps

# test
haystack = "AABABAAAABA"
needle = "AAAB"
print(findStr(haystack, needle))
