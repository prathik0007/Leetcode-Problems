class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                if nums1[i] not in result:
                    result.append(nums1[i])
        return result
        