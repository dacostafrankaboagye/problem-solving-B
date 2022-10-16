'''
Given the head of a linked list, 
return the list after sorting it in ascending order.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeSort(arr):
    if len(arr)>1:
        m = len(arr) // 2
        l = arr[:m]
        r = arr[m:]
        mergeSort(l)
        mergeSort(r)
        li = 0
        ri = 0
        ai = 0
        while li < len(l) and ri < len(r):
            if l[li] < r[ri]:
                arr[ai] = l[li]
                li += 1
            else:
                arr[ai] = r[ri]
                ri +=1
            ai +=1
        while li < len(l):
            arr[ai] = l[li]
            li += 1
            ai +=1
        while ri < len(r):
            arr[ai] = r[ri]
            ri +=1
            ai += 1



class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current= head
        reList = []
        while current != None:
            data = current.val
            reList.append(data)
            current = current.next

        #sort the list
        mergeSort(reList)

        # change the sorted list to listNode
        result = ListNode(0)
        temp = result
        print(reList)
        for i in range(len(reList)):
            data = reList[i]
            temp.next = ListNode(reList[i])
            temp = temp.next

        return result.next
        



        # reverse

