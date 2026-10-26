class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        res = len(set(candyType))
        count = len(candyType) // 2
        return min(res, count)
        