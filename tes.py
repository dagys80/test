''' У вас есть длинная клумба, в которой некоторые участки засажены, а некоторые нет. Однако цветы нельзя сажать на соседних участках.

Дан целочисленный массив, flowerbedсодержащий 0' и 1', где 0означает пустой, а 1означает непустой, и целое число n, вернуть , можно true ли n посадить новые цветы в , flowerbed не нарушая правила отсутствия смежных цветов, и false в противном случае .

 

Пример 1:

Вход: клумба = [1,0,0,0,1], n = 1
 Выход: истина
Пример 2:

Вход: клумба = [1,0,0,0,1], n = 2
 Выход: false
 

Ограничения:

1 <= flowerbed.length <= 2 * 104
flowerbed[i]это 0или 1.
В . нет двух соседних цветков flowerbed.
0 <= n <= flowerbed.length'''
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)

        for i in range(length):
            if flowerbed[i] == 0:
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == length - 1 or flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1

                    if count >= n:
                        return True

        return count >= n

#test
sol = Solution()
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))  #true
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))  #false