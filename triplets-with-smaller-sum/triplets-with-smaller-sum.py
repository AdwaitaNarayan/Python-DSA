class Solution:
    def countTriplets(self, sum, arr):
        #code here
        
        arr.sort()
        n = len(arr)
        count = 0
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                if arr[i] + arr[l] + arr[r] < sum:
                    count += r - l
                    l += 1
                else:
                    r -= 1
        return count       