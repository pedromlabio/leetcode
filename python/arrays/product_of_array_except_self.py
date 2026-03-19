class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        reversed_list = nums.copy()
        reversed_list.reverse()
        prefixes = [nums[0]]

        for i in range(1, len(nums)):
            prefixes.append(prefixes[i-1] * nums[i])
        
        sulfixes = [reversed_list[0]]
        for i in range(1, len(reversed_list)):
            sulfixes.append(sulfixes[i-1] * reversed_list[i])
        
        sulfixes.reverse()

        product = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                #start
                product[i] = sulfixes[1]
                continue
            elif i == len(nums) - 1:
                product[i] = prefixes[i-1]
                continue
            
            product[i] = prefixes[i-1] * sulfixes[i+1]
        
        return product