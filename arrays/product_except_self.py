# Problema: Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Responsável: Zanatta
# Tempo: O(n) | Espaço: O(1) extra (answer não conta)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # inicializa com 1 pois é neutro na multiplicação

        # Left products
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        # Right products
        right = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
