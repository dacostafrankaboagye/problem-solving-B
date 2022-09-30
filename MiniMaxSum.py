
'''
Given five positive integers, find the minimum and maximum values that can be calculated by 
summing exactly four of the five integers. Then print the respective minimum and maximum values 
as a single line of two space-separated long integers.
'''







#________ my sol

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    mini = arr[ : -1]
    maxi = arr[ 1: ]

    print(sum(mini), sum(maxi))
    
    
    
    
    
    
