'''

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''




def performTracking(ans, nums, subSet, idx):
    ans.append(subSet[:])
    for i in range(idx, len(nums)):
        subSet.append(nums[i])
        performTracking(ans, nums, subSet, i+1)
        subSet.pop(-1)
    return



class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans =[]
        subSet = []
        idx = 0
        performTracking(ans, nums, subSet, idx)
        return ans
