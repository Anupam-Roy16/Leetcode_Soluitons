# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp_list = []
        while head:
            temp_list.append(head.val)
            head = head.next
        if temp_list == temp_list[::-1]:
            return True
        else:
            return False
        