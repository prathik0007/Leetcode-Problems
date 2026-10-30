class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        answer = []
        words = words.copy()
        for char in words[0]:
            count = 0
            for i in range(len(words)):
                if char in words[i]:
                    count += 1
                    words[i] = words[i].replace(char, "", 1)
            if count == len(words):
                answer.append(char)
        return answer

