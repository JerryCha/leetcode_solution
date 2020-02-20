# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        recursive = False
        if not recursive:
            # n: the number of nodes between rear and front pointer (inclusive).
            front = head
            back = None
            backPrev = None
            
            while front != None:
                n -= 1
                if n == 0:
                    back = head
                elif n < 0:
                    backPrev = back
                    back = back.next
                front = front.next
                
            if back is None or backPrev is None:
                return head.next
            backPrev.next = back.next
        else:
            n = self.recursiveWay(head, n)
            if n >= 0:
                return head.next
        return head
    
    def recursiveWay(self, head: ListNode, n: int) -> int:
        if head.next is not None:
            n = self.recursiveWay(head.next, n)
        if n == 0:
            head.next = head.next.next
        return n-1

def test():
    l = [1,2,3,4,5]
    head = None
    curr = None
    for i in range(len(l)):
        if head is None:
            head = ListNode(l[i])
            curr = head
        else:
            curr.next = ListNode(l[i])
            curr = curr.next
    s = Solution()
    head = s.removeNthFromEnd(head, 1)
    curr = head
    res = []
    while curr is not None:
        res.append(curr.val)
        curr = curr.next
    print(res)

test()