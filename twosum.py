class Solution:

    def twoum(self, nums: list[int], target: int) -> list[int]:
        
        temp = {}

        for i, n in enumerate(nums):
            answer = target - n
            if answer in temp:
                j = temp[answer]
                return [j, i]
            temp[n] = i


