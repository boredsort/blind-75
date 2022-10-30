class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        temp = {}

        for i, n in enumerate(nums):
            answer = target - n
            if answer in temp:
                j = temp[answer]
                return [j, i]
            temp[n] = i



s = Solution()
nimal = [1,4]
sol = s.twoSum(nimal, 5)
print(sol)