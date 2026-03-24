class Solution:
        #submitted only on neetcode due to lack of leetcode premium
    def encode(self, strs: List[str]) -> str:

        #should be O(n)
        string_encode = ""
        full_text = ""
        for string in strs:
            string_encode = string_encode + str(len(string)) + "#"
            full_text = full_text + string
        string_encode = string_encode + "#_#_#" + full_text

        return string_encode

    def decode(self, s: str) -> List[str]:
        obj = s.split("#_#_#", 1) # the max split one makes sure we won't have problems with the string having the decode delimiter
        lens = obj[0]
        strings = obj[1]
        lens = lens.split("#")
        len_num = []
        lens.pop() #removing the last value as it's empty
        for i in lens:
            len_num.append(int(i))
        
        decoded_strings = []
        for size in len_num:
            decoded_strings.append(strings[:size])
            strings = strings[size:]
        
        return decoded_strings