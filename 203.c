/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode* prev = NULL;
    struct ListNode* curr = head;
    
    while (curr != NULL) {
        if (curr->val == val) {
            if (curr == head) {
                head = head->next;
                curr = curr->next;
            } else {
                curr = curr->next;
                prev->next = curr;
            }
        } else {
            if (prev == NULL)
                prev = head;
            else
                prev = prev->next;
            curr = curr->next;
        }
    }
    
    return head;
}
