class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        c = []
        for i in nums:
            c.append(i * i)

        return (sorted(c))
