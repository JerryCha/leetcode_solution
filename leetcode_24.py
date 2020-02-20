# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs1(self, head: ListNode) -> ListNode:
        # Case where reaching the end of list or accept a None. (Base case)
        if not head or not head.next:
            return head
        '''
            We continuously swap divide the list into two parts, 
            former of which has two nodes to swap 
            whereas the remaining which will pass to itself and process by the same procedure.
        ''' 
        # As guaranteed by the function, it will return a swapped list's head.
        # Therefore, we can assume that subsequent nodes have been correctly swapped.
        nextHead = self.swapPairs1(head.next.next)
        # We assign a temporary pointer referring to the head of this section of list.
        temp = head
        # Now, it is safe to redirect the head by moving head one node further.
        head = temp.next
        # When reached this line, head has pointed to the next of its old node.
        # We now assign its next to the temp, which is its old predecessor.
        head.next = temp
        # Finished off by connecting the swapped part.
        temp.next = nextHead
        # Return the heading node.
        return head

    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        curr = head
        prev = None
        head = head.next
        while curr and curr.next:
            temp = curr # Create a temporary pointer referring to the first node
            curr = curr.next    # Let the curr pointer move further
            # Now, curr should have been at the second swapped node
            temp.next = curr.next   # Get ready for swapping by redirecting the first node's next to the head of next block
            curr.next = temp    # It's safe to let the second node be the new head of current block.
            # Finally, reconnect this block to the previous one
            if prev:
                prev.next = curr
            prev = temp
            curr = temp.next
        return head