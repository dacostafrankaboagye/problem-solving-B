'''
Two Sums



Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


HINTS
A really brute force way would be to search for 
all possible pairs of numbers but that would be too slow. 
Again, it's best to try out brute force solutions for just for completeness. 
It is from these brute force solutions that you can come up with optimizations.

So, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y which is value - x
where value is the input parameter. Can we change our array somehow so that this search becomes faster?

'''
