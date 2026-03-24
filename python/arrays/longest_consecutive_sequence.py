class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #ik what sets were but didn't realize how useful they could be
        if not nums: return 0 #edge case

        setted_list = set(nums)
        longest = 0
        k = 0

        for num in setted_list:
            if num - 1 not in setted_list: #only count if in start of the sequence
                k = 1
                while num + k in setted_list:
                    k+=1
                longest = max(k, longest)
        
        return longest
