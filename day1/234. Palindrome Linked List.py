Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Helper function to reverse a linked list
        def reverse_list(node):
            prev = None
            current = node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # Find the middle of the linked list using the slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        second_half_reversed = reverse_list(slow)

        # Compare the first half and reversed second half
        while second_half_reversed:
            if head.val != second_half_reversed.val:
                return False
            head = head.next
            second_half_reversed = second_half_reversed.next

        return True
