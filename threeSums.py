'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example::
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''




def partition(arr, low, high):
    piv = arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j] <= piv:
            arr[j],arr[i] = arr[i], arr[j]
            i = i+1
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1




def tracking(res, nums, subSet, idx):
    
    if len(subSet) == 3 and sum(subSet)==0:
        subSet = sorted(subSet)
        print(subSet)
        if subSet not in res:
            res.append(subSet[:])
    for i in range(idx, len(nums)):
        subSet.append(nums[i])
        tracking(res,nums,subSet, i+1)
        subSet.pop(-1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        # soln 1 -  long time -- time limit exceeded
        res = []
        subSet = []
        idx  = 0
        tracking(res, nums, subSet, idx)
        return res
        '''

        # another approach
        if len(nums) < 3:
            return []
        else:
            result = []
            nums = sorted(nums)
            for i in range(0, len(nums)-2):
                start = i+1
                end = len(nums) -1
                while start < end:
                    theSum = nums[i] + nums[start] + nums[end]
                    if theSum == 0:
                        temp = (nums[i] , nums[start] , nums[end])
                        result.append(temp)
                        start +=1
                        end -= 1
                    elif theSum < 0:
                        start +=1 
                    elif theSum > 0:
                        end -=1
            return [list(i) for i in set(result)]

        



