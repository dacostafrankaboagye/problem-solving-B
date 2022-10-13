'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


'''


#online solution
def twoNumberSum(array, targetSum):
    # Save the number seen so far
    seen = set()
    # Traverse the array
    for n in array:
      	# Assume n is the first number
        n2 = targetSum - n  # Calcualte which is the other number needed
        seen.add(n)  # Keep track of all the seen numbers
        if n2 != n and n2 in seen:
            return [n, n2]  # Found it
            
	return []




# My Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        idxArray = []
        newArray = nums.copy()

        for i in nums:
            idx = nums.index(i)
            numToSearch = target - i
            temp = nums[idx]
            nums[idx] = " "
            if (numToSearch in nums) :
                idxArray.append(idx)
                temp = nums[idx]
                nums[idx] = " "
                if (numToSearch in nums) :
                    idx2 = nums.index(numToSearch)
                    idxArray.append(idx2)
                    break
            nums[idx] = temp
    
                
        return set(idxArray)


































