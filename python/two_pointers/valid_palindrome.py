import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #first make everything lower
        #defining our own var
        string = s.lower()

        #regex noooo
        string = re.sub(r'[^a-zA-Z0-9]', '', string)

        #now we get two pointers
        #first we check if the string len is odd or even
        size = len(string)
        isEven = not (size % 2) #bear with me now
        rightIndex = 0
        leftIndex = 0
        middle = size//2
        if isEven:
            rightIndex = middle
            leftIndex = rightIndex-1
        else:
            rightIndex = middle + 1
            leftIndex = middle - 1

        while (leftIndex+1): #the realization
            if string[leftIndex] != string[rightIndex]:
                return False
            leftIndex-=1
            rightIndex+=1

        return True
