from collections import Counter #how DID I NOT KNOW ABOUT LIBS TO MAKE LIFE EASIER
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums) #getting da frequencies

        common = freqs.most_common(k) #this is literally child's play :broken_heart:

        result = [element for element, count in common] #THIS IS HUGE VERY IMPORTANT I SHOULD PROB REMEMBER THIS

        return result
