class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
            
        def mergeTwo(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 if l1 else l2
            return dummy.next
            
        interval = 1
        amount = len(lists)
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = mergeTwo(lists[i], lists[i + interval])
            interval *= 2
            
        return lists[0]
