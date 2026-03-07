class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Nˆ2 gave me timelimit, saw a comment talking about sorting the list which would then allow for a N approach(plus the sorting ofc)
        #oh it's python I don't need to implement a sorting alg

        #current solution may not have the best runtime, but it's memory efficient, tradeoff
        nums.sort()
        for i in range(len(nums)):
            if i + 1 == len(nums): continue #avoid trying to access a non existing index
            if nums[i] == nums[i + 1]: return True




        return False