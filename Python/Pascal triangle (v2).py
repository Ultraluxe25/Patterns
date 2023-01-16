"""
Дано целое число n. Выведите n строк треугольника Паскаля без форматирования.

Подсказка: Поищите формулу сочетаний для чисел треугольника Паскаля и примените ее.

Ввод:

n – ряд треугольника Паскаля

Вывод:

Треугольник Паскаля до заданного ряда

Sample Input:
3

Sample Output:
1
11
121
"""

class PascalTriangle:
    def __init__(self, length: int) -> None:
        self.length = length
        
    def __make_ones_triangle(self) -> list[list[int]]:
        triangle = []
        for i in range(self.length):
            tier = [1] * (i + 1)
            triangle.append(tier)
        return triangle
    
    def __fill_triangle(self) -> list[list[int]]:
        self.triangle = self.__make_ones_triangle()
        for i in range(2, self.length):
            for j in range(1, i):
                self.triangle[i][j] = self.triangle[i - 1][j - 1] + self.triangle[i - 1][j]
        return self.triangle
    
    def __make_each_element_string_in_triangle(self) -> list[list[str]]:
        self.triangle = self.__fill_triangle()
        for tier in self.triangle:
            for index,element in enumerate(tier):
                tier[index] = str(element)
        return self.triangle
        
    def draw_triangle(self) -> None:
        self.triangle = self.__make_each_element_string_in_triangle()
        for tier in self.triangle:
            print(''.join(tier))    
            
            
tiers = int(input())        
user_triangle = PascalTriangle(tiers)
user_triangle.draw_triangle()
