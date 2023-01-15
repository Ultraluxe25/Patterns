"""
Напишите программу, которая переводит число в систему счисления с основанием 5.

Ввод:

n – число в десятичной системе счисления в промежутке от [0..\infty][0..∞]

Вывод:

res – число в пятеричной системе счисления

Sample Input:
12

Sample Output:
22
"""

def change_number_system(number: int, number_system=5) -> str:
    if number == 0:
        return '0'
    result = ''
    while number:
        result += str(number % number_system)
        number //= number_system
    return result[::-1]


num = int(input())
print(change_number_system(num))
