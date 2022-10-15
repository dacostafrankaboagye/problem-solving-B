

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
        sum = 0

        rec(l1)
        sum += int(ans)
        ans = ""
        rec(l2)
        sum += int(ans)
        ans = ""
        sum = str(sum)
        sum = sum[::-1]
        print(sum)

        for i in range(len(sum)):
            data = sum[i]
            pointer.next = ListNode(data)
            pointer = pointer.next
        return result.next




        
        
