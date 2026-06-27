class Solution:
    def addDigits(self, num: int) -> int:
        # Keep looping until num becomes a single digit
        while num > 9:
            # Convert num to string, turn each character back to int, and sum them
            num = sum(int(digit) for digit in str(num))
            
        return num
        