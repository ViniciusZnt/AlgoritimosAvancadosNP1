# Problema: Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/
# Responsável: Zanatta
# Tempo: O(n) | Espaço: O(1)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nextNode = None

        while head:
            temp      = head.next   # 1. Guarda o próximo nó
            head.next = nextNode    # 2. Inverte a seta (aponta para trás)
            nextNode  = head        # 3. Avança o "novo início"
            head      = temp        # 4. Avança para o próximo nó original

        return nextNode
