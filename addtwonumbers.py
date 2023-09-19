class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Initialize output list with a dummy node
        dummy_node = ListNode()
        current_node = dummy_node
        carry = 0

        # Loop until we have completely processed both lists and the carry
        while l1 or l2 or carry:
            # Get the values of the current nodes, or 0 if the list is exhausted
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)

            # Calculate the sum and the carry
            sum_of_values = val1 + val2 + carry
            carry = sum_of_values // 10

            # Store the result in the current node
            current_node.next = ListNode(sum_of_values % 10)

            # Move to the next node
            current_node = current_node.next

            # Move to the next nodes in the input lists
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        # The first node was a dummy node, so return the next node
        return dummy_node.next