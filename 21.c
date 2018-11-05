/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    if (l1 == NULL && l2 == NULL)
        return NULL;
    else if (l1 == NULL && l2 != NULL)
        return l2;
    else if (l1 != NULL && l2 == NULL)
        return l1;
    else {
        // Initialize head pointer, referring to l1's head.
        struct ListNode *head = l1;
        // Moving l1 to the end of list.
        while (l1->next != NULL)
            l1 = l1->next;
        // Connect l2 to the end of l1
        l1->next = l2;
        
        // Sort the list
        struct ListNode *position = head;
        while (position->next != NULL) {
            struct ListNode *cursor = position->next;
            struct ListNode *min_cursor = position;
            while (cursor) {
                //printf("current position: %d, cursor: %d\n", position->val, cursor->val);
                if (cursor->val < min_cursor->val)
                    min_cursor = cursor;
                cursor = cursor->next;
            }
            int min = min_cursor->val;
            min_cursor->val = position->val;
            position->val = min;
            position = position->next;
        }
        
        return head;
    }
}
