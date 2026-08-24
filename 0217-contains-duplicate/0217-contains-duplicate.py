class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        set1 = set(nums)
        print(set1)
        return len(nums) != len(set1)
