'''Вам даны две строки word1и word2. Объедините строки, добавляя буквы в чередующемся порядке, начиная с word1. Если строка длиннее другой, добавьте дополнительные буквы в конец объединенной строки.

Верните объединенную строку.
Пример 1:

Ввод: word1 = "abc", word2 = "pqr"
 Вывод: "apbqcr"
 Пояснение:  Объединенная строка будет объединена следующим образом:
слово1: азбука
слово2: pqr
объединено: apbqcr
Пример 2:

Ввод: word1 = "ab", word2 = "pqrs"
 Вывод: "apbqrs"
 Пояснение:  Обратите внимание, что поскольку word2 длиннее, в конец добавляется "rs".
слово1: аб
слово2: pqrs
объединено: apbqrs
Пример 3:

Ввод: word1 = "abcd", word2 = "pq"
 Вывод: "apbqcd"
 Пояснение:  Обратите внимание, что поскольку word1 длиннее, в конец добавляется "cd".
слово1: abcd
слово2: pq
объединено: apbqcd
 

Ограничения:

1 <= word1.length, word2.length <= 100
word1и word2состоят из строчных английских букв.     '''   

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
        return "".join(merged)


solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))
print(solution.mergeAlternately("ab", "pqrs"))
print(solution.mergeAlternately("abcd", "pq"))