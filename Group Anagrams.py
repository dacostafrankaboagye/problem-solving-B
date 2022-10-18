
'''


Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


'''






class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        if len(strs) == 1:
            return [strs]
        result = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in result:
                result[sortedWord] = [word]
            else:
                result[sortedWord] = result[sortedWord] + [word]
        return [result[item] for item in result]










