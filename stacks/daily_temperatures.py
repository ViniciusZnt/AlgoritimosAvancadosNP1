# Problema: Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures/
# Responsável: Zanatta
# Tempo: O(n) | Espaço: O(n)
# Técnica: Pilha Monotônica (Monotonic Stack)

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # desempilha enquanto a temperatura atual for maior que a do topo
            while st and temperatures[i] > temperatures[st[-1]]:
                idx = st.pop()
                res[idx] = i - idx  # diferença de dias
            st.append(i)            # empilha o índice, não o valor

        return res
