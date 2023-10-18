# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that
# there is a bijection between a letter in patternand a non-empty word in s.

def wordPattern(pattern: str, s: str) -> bool:
    words = s.split(' ')
    ref_dict = {}
    ref_set = set()
    len_pattern = len(pattern)
    if len_pattern != len(words):
        return False
    for i in range(len_pattern):
        if not ref_dict.get(pattern[i]):
            if words[i] not in ref_set:
                ref_dict[pattern[i]] = words[i]
                ref_set.add(words[i])
            else:
                return False
        elif words[i] != ref_dict[pattern[i]]:
            return False
    return True


pattern = "abba"
s = "dog cat cat dog"
assert wordPattern(pattern, s) == True


pattern = "abba"
s = "dog cat cat fish"
assert wordPattern(pattern, s) == False


pattern = "aaaa"
s = "dog cat cat dog"
assert wordPattern(pattern, s) == False

pattern = "aaa"
s = "aa aa aa aa"
assert wordPattern(pattern, s) == False