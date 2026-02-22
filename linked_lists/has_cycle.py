# Problema: Linked List Cycle
# Link: https://leetcode.com/problems/linked-list-cycle/
# Responsável: Zanatta
# Tempo: O(n) | Espaço: O(1)
# Algoritmo: Floyd's Cycle Detection (tartaruga e lebre)

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next        # anda 1 passo
            fast = fast.next.next   # anda 2 passos

            if slow == fast:        # se se encontraram, há ciclo
                return True

        return False
