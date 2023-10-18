# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character
#     while preserving the order of characters. No two characters may map to the same character,
#     but a character may map to itself.
def isIsomorphic(s: str, t: str) -> bool:
    ref_dict = {}
    ref_set = set()
    len_s = len(s)
    for i in range(len_s):
        if not ref_dict.get(s[i]):
            if t[i] not in ref_set:
                ref_set.add(t[i])
                ref_dict[s[i]] = t[i]
            else:
                return False
        elif ref_dict.get(s[i]) != t[i]:
            return False
    return True

s = "egg"
t = "add"
assert isIsomorphic(s, t) == True

s = "foo"
t = "bar"
assert isIsomorphic(s, t) == False

s = "paper"
t = "title"
assert isIsomorphic(s, t) == True