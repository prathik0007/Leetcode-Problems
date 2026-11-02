class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        large = max(nums)
        answer = []
        for num in range(small,large+1):
            if num not in nums:
                answer.append(num)
        return answer
        