# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    group_dict = {}
    for w in strs:
        key = [0] * 26
        for c in w:
            key[ord(c) - ord('a')] += 1
        if not group_dict.get(tuple(key)):
            group_dict[tuple(key)] = []
        group_dict[tuple(key)].append(w)
    return group_dict.values()

strs = ["eat","tea","tan","ate","nat","bat"]
# assert groupAnagrams(strs) == [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = [""]
# assert groupAnagrams(strs) == [[""]]

strs = ["a"]
# assert groupAnagrams(strs) == [["a"]]