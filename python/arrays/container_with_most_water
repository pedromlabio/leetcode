class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        cur_water = 0
        lowest_base = 0
        pointer_left = 0
        pointer_right = len(height) - 1
        while pointer_left != pointer_right:
            # first we calculate current water
            lowest_base = height[pointer_left]
            if height[pointer_right] < lowest_base:
                lowest_base = height[pointer_right]
            cur_water = (pointer_right - pointer_left) * lowest_base
            if cur_water > max_water:
                max_water = cur_water

            # moving the pointer with the lowest base
            if height[pointer_left] < height[pointer_right]:
                # increase pointer left
                pointer_left+=1
            else:
                # decrease pointer right
                pointer_right-=1 
        return max_water