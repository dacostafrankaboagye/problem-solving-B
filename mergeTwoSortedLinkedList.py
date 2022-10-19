'''
21. Merge Two Sorted Lists
Easy
15.5K
1.4K
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]


'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def partition(arr, low, high):
    pivot = arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
    



def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr,low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        theList1 = []
        theList2 = []
        temp1 = list1
        temp2 = list2
        while temp1 or temp2:
            if temp1:
                theList1.append(temp1.val)
                temp1 = temp1.next
            if temp2:
                theList2.append(temp2.val)
                temp2 = temp2.next
        #print(theList1)
        #print(theList2)
        joinedList = theList1 + theList2
        print(joinedList)
        #print(sorted(joinedList))
        quickSort(joinedList, 0, len(joinedList)-1)
        print(joinedList)
        # construct the Linked List
        res = ListNode(0)
        temp = res
        for i in range(0, len(joinedList)):
            temp.next = ListNode(joinedList[i])
            temp = temp.next
        return res.next


        
        






















