# Problema: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Responsável: Zanatta
# Tempo: O(n) | Espaço: O(n)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in val_idx:
                return [val_idx[complement], i]
            val_idx[num] = i
