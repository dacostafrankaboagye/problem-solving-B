'''
Longest Substring Without Repeating Character
Given a string s, find the length of the longest substring without repeating characters.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        subString=""
        for i in range(0, len(s)):
            if s[i] not in subString:
                subString += s[i]
                maxCount = max(maxCount, len(subString))
            else:
                subString = subString.split(s[i])[1]
                subString+= s[i]
                maxCount = max(maxCount, len(subString))
        return maxCount
