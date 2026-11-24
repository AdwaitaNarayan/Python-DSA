class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        l = 0
        n = len(nums)
        r = n-1
        sub = []
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = n-1

            while l<r:
                t = nums[i]+nums[r]+nums[l]

                if t == 0:
                    sub.append([nums[i],nums[l],nums[r]])

                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l<r and nums[r] == nums[r+1]:
                        r -= 1

                elif t<0:
                    l += 1
                else:
                    r -= 1
                
        return sub

        