"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # new linked list for the sum of the other two
        new_head = ListNode(0)
        # pointer on linked list 1, starts at head
        p1 = l1
        # pointer on linked list 2
        p2 = l2
        # pointer on new linked list
        current = new_head
        # the amount to carry over
        carry = 0

        # while either pointer is still pointing at something
        while (p1 is not None) or (p2 is not None):
            # if p1 is still pointing at a value
            if (p1 is not None):
                # x = that value
                x = p1.val
            # if p1 is None
            else:
                # x = 0 as we still have something at p2
                x = 0
            # the same as the p1 logic
            if (p2 is not None):
                y = p2.val
            else:
                y = 0
            
            # math
            sum = x + y + carry
            # sense each node is only a single digit, gotta carry
            carry = sum // 10
            # make the next node in the list
            current.next = ListNode(sum % 10)

            # set the current pointer to the new current
            current = current.next
            # set p1 and p2 to the new pointer spot.
            if (p1 is not None): 
                p1 = p1.next
            if (p2 is not None):
                p2 = p2.next

        # one the while loop stops, if there is still a carry, at it to the new list
        if carry > 0:
            current.next = ListNode(1)

        # return the new list (.next is to cut off the 0 at the head)
        return new_head.next

            