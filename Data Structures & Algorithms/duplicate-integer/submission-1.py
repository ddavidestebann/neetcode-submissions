class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        order = list(set(nums))
        order.sort()
        nums.sort()

        if order == nums:
            sol = False
        else:
            sol = True
        return sol

        