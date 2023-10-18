# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or
# phrase, typically using all the original letters exactly once.
def isAnagram(s: str, t: str) -> bool:
    if (len(s) != len(t)):
        return False

    ref_dict = {}
    for c in s:
        ref_dict[c] = ref_dict.get(c, 0) + 1

    for c in t:
        if ref_dict.get(c, 0) == 0:
            return False
        ref_dict[c] -= 1
    return True


s = "anagram"
t = "nagaram"
assert isAnagram(s, t) == True

s = "rat"
t = "car"
assert isAnagram(s, t) == False