class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        original_size = len(nums) #this might not even be needed but i'm not very sure
        indexes = []
        index_offset = 0
        for i in range(original_size):
            if nums[i] == val:
                indexes.append(i + index_offset)
                index_offset-=1
        k = original_size - len(indexes)
        for value in indexes:
            nums.pop(value)
        
        return k