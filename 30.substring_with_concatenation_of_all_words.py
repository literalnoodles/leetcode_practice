# You are given a string s and an array of strings words. All the strings of words are of the same length.
# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.
#     For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab"
#       are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
# Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.
from typing import List

def findSubstring(s: str, words: List[str]) -> List[int]:
    reference_dict = {}
    for word in words:
        if word in reference_dict:
            reference_dict[word] += 1
        else:
            reference_dict[word] = 1
    l = 0
    result = []
    word_len = len(words[0])
    str_len = word_len * len(words)
    compare_dict = {}
    while l <= len(s) - str_len:
        compare_dict.clear()
        found = True
        for i in range(len(words)):
            substr = s[l + i * word_len: l + (i+1) * word_len]
            if substr not in (reference_dict):
                found = False
                break
            compare_dict[substr] = compare_dict.get(substr, 0) + 1
            if (compare_dict[substr] > reference_dict[substr]):
                found = False
                break
        if found:
            result.append(l)
        l += 1
    return result

s = "barfoothefoobarman"
words = ["foo","bar"]
assert findSubstring(s, words) == [0, 9]

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
assert findSubstring(s, words) == []

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
assert findSubstring(s, words) == [6, 9, 12]
