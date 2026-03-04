class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j: continue
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        # code should never get here
        print("error, couldn't find value")
        return [0, 0]