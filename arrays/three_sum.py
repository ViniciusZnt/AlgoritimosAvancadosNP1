# Problema: 3Sum
# Link: https://leetcode.com/problems/3sum/
# Responsável: Zanatta
# Tempo: O(n²) | Espaço: O(1)

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # pula duplicatas do elemento fixado
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                soma = nums[i] + nums[left] + nums[right]

                if soma == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # pula duplicatas dos dois ponteiros
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

                elif soma < 0:
                    left += 1
                else:
                    right -= 1

        return result
