class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()

        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        # return len(nums)

        # num_set = set(nums)
        # n = len(nums)
        # for i in range(n + 1):
        #     if i not in num_set
        #         return i

        n = len(nums)
        xorr = n
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr
        