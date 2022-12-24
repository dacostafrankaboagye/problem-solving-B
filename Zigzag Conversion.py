'''
The string "PAYPALISHIRING" is written in a zigzag 
pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

'''

# my soln

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strCopy = s
        d  = {}
        backNumRows = numRows - 2
        pointer = 0
        lenCounter = 0
        backPointer = numRows -1
        def createD(numRows,d):
            for i in range(numRows):
                d[i] = ""
            return d
        
        #print(d)
        createD(numRows, d)
        if(len(s) > numRows):
            

            while lenCounter  < len(s):
                for i in range(0, numRows):
                    d[i] = d[i] + s[lenCounter]
                    lenCounter +=1
                #print(d)

                if backNumRows > 0:
                    #print(backNumRows)
                    for i in range(backNumRows,0,-1):
                        try:
                            d[i] = d[i] + s[lenCounter]
                            lenCounter +=1
                        except:
                            break
                #print(d)
                
                strCopy = s[lenCounter:]
                if len(strCopy) < numRows:
                    numRows = len(strCopy)
                    backNumRows = 0
                #print("...." ,len(strCopy))

        else:
            for i in range(0, len(s)):
                d[i] = d[i] + s[lenCounter]
                lenCounter +=1

        values = ''.join(d.values())
        print(values)
        return values
    
            






