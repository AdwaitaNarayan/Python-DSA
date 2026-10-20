class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i , num in enumerate(numbers):
            s = target-num
            if s in dic:
                return [dic[s]+1, i+1]
            dic[num]=i
        


        