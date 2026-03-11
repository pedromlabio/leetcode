class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grouped = []
        sorted_words = []
        for i in range(len(strs)):
            #first thing we do is check in the sorted words
            s_word = sorted(strs[i])
            index = -1
            if s_word in sorted_words:
                index = sorted_words.index(s_word)
            if index >= 0:
                #add to the grouped list
                grouped[index].append(strs[i])
            else:
                #new word that should be added in the sorted_words and grouped lists
                sorted_words.append(s_word)
                grouped.append([strs[i]])
        return grouped
