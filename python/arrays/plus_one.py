class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1
        carry = True

        while carry:

            if pointer < 0:
                #we need to add an extra 1 at the start of the array
                digits.insert(0, 1)
                carry = False
                continue

            #first we calculate the +1
            plus_one = digits[pointer] + 1
            if plus_one >= 10:
                #carry
                digit = plus_one - 10
                digits[pointer] = digit
                pointer-=1
            else:
                #no carry
                carry = False
                digits[pointer] = plus_one


        return digits