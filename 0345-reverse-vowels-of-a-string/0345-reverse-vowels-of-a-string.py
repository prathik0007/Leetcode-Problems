class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        answer = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if answer[left] not in vowels:
                left += 1
            elif answer[right] not in vowels:
                right -= 1
            else:
                answer[left], answer[right] = answer[right], answer[left]
                left += 1
                right -= 1
        return "".join(answer)