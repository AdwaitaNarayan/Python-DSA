class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digit = "123456789"
        ans = []

        for i in range(2, 10):

            #starting postion
            for j in range(0, 10-i):
                num = int(digit[j:j + i])
                
                if low <= num <= high:
                    ans.append(num)
        return ans