'''Для двух строк sи tмы говорим « tделится s» тогда и только тогда, когда s = t + t + t + ... + t + t(т.е. tконкатенируется сама с собой один или более раз).

Для двух строк str1и str2вернуть наибольшую строку x, которая xделит str1иstr2 .

 

Пример 1:

Ввод: str1 = "ABCABC", str2 = "ABC"
 Вывод: "ABC"
Пример 2:

Вход: str1 = "ABABAB", str2 = "ABAB"
 Выход: "AB"
Пример 3:

Вход: str1 = "LEET", str2 = "CODE"
 Выход: ""
 

Ограничения:

1 <= str1.length, str2.length <= 1000
str1и str2состоят из заглавных английских букв.'''
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]

solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))  
print(solution.gcdOfStrings("ABABAB", "ABAB"))  
  
