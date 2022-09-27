'''

Given an array of integers, 
calculate the ratios of its elements that are positive, 
negative, and zero. Print the decimal value of each fraction on a 
new line with   6 places after the decimal.

'''
#__________________________________________________________

'''
My solution
'''

def plusMinus(arr):
    # Write your code here
    sumPositive = 0
    sumNegative = 0
    sumZeros = 0
    for theNumber in arr:
        if theNumber == 0:
            sumZeros +=1;
        if theNumber < 0:
            sumNegative +=1
        if theNumber > 0:
            sumPositive +=1;
    ratioPostive = sumPositive/len(arr)
    ratioNegative = sumNegative/len(arr)
    ratioZeros = sumZeros/len(arr)
    print('{:.6f}\n{:.6f}\n{:.6f}'.format(ratioPostive, ratioNegative, ratioZeros))
    
    
    
    
    
    
    #______________________________
    
    '''
    Online solution
    
    '''
    
    def positiveNegativeZero(arr):
 
    # Store the array length into the variable len.
    length = len(arr);
 
    # Initialize the postiveCount, negativeCount, and
    # zeroCountby 0 which will count the total number
    # of positive, negative and zero elements
    positiveCount = 0;
    negativeCount = 0;
    zeroCount = 0;
 
    # Traverse the array and count the total number of
    # positive, negative, and zero elements.
    for i in range(length):
        if (arr[i] > 0):
            positiveCount += 1;
        elif(arr[i] < 0):
            negativeCount += 1;
        elif(arr[i] == 0):
            zeroCount += 1;
         
    # Print the ratio of positive,
    # negative, and zero elements
    # in the array up to four decimal places.
    print("{0:.4f}".format((positiveCount / length)), end=" ");
    print("%1.4f "%(negativeCount / length), end=" ");
    print("%1.4f "%(zeroCount / length), end=" ");
    print();
    
    
