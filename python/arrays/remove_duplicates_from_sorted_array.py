class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #lesgo
        nums.sort() #sorting
        index_offset = 0
        indexes = []
        k = 0
        last_val = None
        for i in range(len(nums)):
            if last_val == nums[i]:
                #repeated and must be removed, store index
                indexes.append(i + index_offset)
                index_offset-=1
            else:
                #new number
                last_val = nums[i]
                k+=1
                continue
        
        for value in indexes:
            nums.pop(value)
        
        return k
