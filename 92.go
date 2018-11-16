/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseBetween(head *ListNode, m int, n int) *ListNode {
    if head == nil {
        return head
    }
    
    node_i := 1
    var before_range, after_range, left_bound, right_bound *ListNode
    temp_head := &ListNode{Val: 0, Next: head}
    
    curr := head
    prev := temp_head
    for curr != nil {
        temp_next := curr.Next
        if node_i == m {
            left_bound = curr
            before_range = prev
        }
        if node_i == n {
            right_bound = curr
            after_range = curr.Next
        }
        if node_i > m && node_i <= n {
            curr.Next = prev
        }
        node_i++
        prev = curr
        curr = temp_next
    }
    before_range.Next = right_bound
    left_bound.Next = after_range
    return temp_head.Next
}
