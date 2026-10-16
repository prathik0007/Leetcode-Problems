
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n):
            substring = s[:i]
            if n % len(substring) == 0:
                count = n // len(substring)
                if substring * count == s:
                    return True
        return False

        