class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for indx, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stackTemp, stackInx = stack.pop()
                ans[stackInx] = (indx - stackInx)
            stack.append([val, indx])
        return ans

        