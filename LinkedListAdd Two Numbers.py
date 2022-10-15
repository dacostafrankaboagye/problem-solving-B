


'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

ans = ""
def rec(l1):
    global ans
    if l1.next == None:
        ans += str(l1.val)
        return  
    else:
        ans += str(l1.val)
        l1 = l1.next
        return rec(l1)



class Solution:


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        pointer = result

        global ans
        sum1 = ""
        sum2 = ""

        rec(l1)
        sum1 = ans 
        ans = ""
        print(sum1)

        rec(l2)
        sum2 = ans
        ans = ""
        print(sum2)

        sum1 = sum1[::-1]
        sum2 = sum2[::-1]
        summ = int(sum1) + int(sum2)
        summ = str(summ)
        summ = summ[::-1]


        for i in range(len(summ)):
            data = summ[i]
            pointer.next = ListNode(data)
            pointer = pointer.next
        return result.next




        
        
