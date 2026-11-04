class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consec = 0
        max = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                consec += 1
                if max < consec:
                    max = consec
            else:
                consec = 0
        return max