class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        n = len(nums)
        for i in range(n):
            r = target - nums[i]
            if r in dic:
                return dic[r], i
            else:
                dic[nums[i]] = i