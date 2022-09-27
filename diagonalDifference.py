'''

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:
1 2 3
4 5 6
9 8 9  

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

'''



#___________________________________________________


'''
My solution
'''

def diagonalDifference(arr):
    # Write your code here
    sumLeft = 0;
    sumRight = 0;
    leftPointer = 0;
    rightPointer = len(arr) - 1;
    for eachColumn in arr:
        sumLeft = sumLeft + eachColumn[leftPointer]
        sumRight = sumRight + eachColumn[rightPointer]
        leftPointer += 1
        rightPointer -= 1
    return abs(sumLeft - sumRight)



#___________________________________________________



'''
Online Solution
'''
def diagonalDifference(arr):
    # Write your code here
    d1 = sum([arr[x][x] for x in range(len(arr))])
    d2 = sum([arr[x][n - 1 - x] for x in range(len(arr))])
    return(abs(d1 - d2)

