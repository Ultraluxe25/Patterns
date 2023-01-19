"""
Напишите функцию, которая в качестве параметра принимает число n и отображает n первых чисел Фибоначчи, не считая 0.

Sample Input:
3

Sample Output:
0 1 1 2
"""

from typing import List


def find_fibonacci(n: int) -> List[int]:
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    elif n == 2:
        return [0, 1, 1]
    
    fb1, fb2 = 1, 1
    result = [0, 1, 1]
    
    for _ in range(n - 2):
        fb1, fb2 = fb2, fb1 + fb2
        result.append(fb2)
        
    return result


members = int(input())
print(*find_fibonacci(members))
