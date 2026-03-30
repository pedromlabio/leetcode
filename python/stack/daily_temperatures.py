class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        size = len(temperatures)
        output = [0] * size

        for i in range(size):
            temp = temperatures[i]
            #check for first number
            if len(stack) == 0: 
                stack.append([temp, i])
                continue
            
            #fun part
            check = True
            while check and len(stack) > 0:
            #first we check if temp is warmer
                if temp > stack[len(stack)-1][0]:
                    #pop and update output
                    old_temp = stack.pop()
                    #getting index
                    start_index = old_temp[1]
                    output[start_index] = i - start_index
                else:
                    check = False
            stack.append([temp, i])
            
        return output
