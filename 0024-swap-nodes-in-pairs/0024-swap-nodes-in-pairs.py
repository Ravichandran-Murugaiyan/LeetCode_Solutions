class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Swap the two nodes
            prev.next = second
            first.next = second.next
            second.next = first

            # Move pointers ahead
            prev = first
            head = first.next

        return dummy.next