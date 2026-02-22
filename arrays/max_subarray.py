# Problema: Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/
# Responsável: Zanatta
# Tempo: O(n) | Espaço: O(1)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        soma = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            soma = max(num, soma + num)
            max_sum = max(max_sum, soma)

        return max_sum
