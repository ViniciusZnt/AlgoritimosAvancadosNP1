# Problema: Remove Nth Node From End of List
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Responsável: Zanatta
# Tempo: O(L) | Espaço: O(1)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy

        # avança fast n+1 posições
        for _ in range(n + 1):
            fast = fast.next

        # move os dois juntos até fast chegar ao fim
        while fast:
            fast = fast.next
            slow = slow.next

        # slow está no nó ANTERIOR ao que deve ser removido
        slow.next = slow.next.next

        return dummy.next
