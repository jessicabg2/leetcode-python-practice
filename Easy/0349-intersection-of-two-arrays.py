class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        # 1. Convert both lists into sets
        set1 = set(nums1)
        set2 = set(nums2)

        # 2. Find the common numbers
        intersection = set1 & set2

        # 3. Convert the intersection into a list
        answer = list(intersection)

        # 4. Return the list
        return answer
