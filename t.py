'''Дана строка s, поменять местами только все гласные в ней и вернуть ее.

Гласные — это 'a', 'e', 'i', 'o', и 'u', и они могут встречаться как в нижнем, так и в верхнем регистре, более одного раза.

 

Пример 1:

Ввод: s = "IceCreAm"

Вывод: "AceCreIm"

Объяснение:

Гласные в s. ['I', 'e', 'e', 'A']При перестановке гласных s становится "AceCreIm".

Пример 2:

Ввод: s = "leetcode"

Вывод: "leotcede"

 

Ограничения:

1 <= s.length <= 3 * 105
sсостоят из печатных символов ASCII.'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return "".join(s)

sol = Solution()
print(sol.reverseVowels("IceCreAm"))
print(sol.reverseVowels("leetcode"))
