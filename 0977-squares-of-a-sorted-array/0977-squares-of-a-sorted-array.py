class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        a = []
        b = []
        # to check for negetive and postive array
        for i in range(len(nums)):
            if nums[i]<0 :
                a.append(nums[i])
            else:
                b.append(nums[i])

        # to check all elements are negetive
        if len(b) == 0:
            for i in range(len(a)):
                a[i] = a[i]*a[i]

            return a[::-1]
        # to check all elements are postive
        elif len(a) == 0:
            for i in range(len(b)):
                b[i] = b[i]*b[i]

            return b

        n = len(a)
        m = len(b)
        i = 0
        j = 0
        l = []
        
        for k in range(n):
            a[k] = a[k]*a[k]
        a = a[::-1]

        for o in range(m):
            b[o] = b[o]*b[o]

        while(i<n and j<m):
            if a[i]<b[j]:
                l.append(a[i])
                i+=1

            else:
                l.append(b[j])
                j+=1
        while(j<m):
            l.append(b[j])
            j+=1
        while(i<n):
            l.append(a[i])
            i+=1
        return l