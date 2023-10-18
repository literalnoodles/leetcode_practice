# Given two strings ransomNote and magazine, return true if
# ransomNote can be constructed by using the letters from magazine
# and false otherwise.
# Each letter in magazine can only be used once in ransomNote

def canConstruct(ransomNote: str, magazine: str) -> bool:
    reference_dict = {}
    for c in magazine:
        reference_dict[c] = reference_dict.get(c, 0) + 1
    for c in ransomNote:
        if reference_dict.get(c, 0) == 0:
            return False
        reference_dict[c] -= 1
    return True

ransomNote = "a"
magazine = "b"
assert canConstruct(ransomNote, magazine) == False

ransomNote = "aa"
magazine = "ab"
assert canConstruct(ransomNote, magazine) == False

ransomNote = "aa"
magazine = "aab"
assert canConstruct(ransomNote, magazine) == True