"""
Вводится 4-х значное число. Если оно является палиндромом, то нужно вывести YES, иначе нужно вывести NO.

Sample Input:
1234

Sample Output:
NO
"""

def palindrom(n):
    if len(n) <= 1:
        return True
    return n[0] == n[-1] and palindrom(n[1:-1])
    

number = input()
print('YES' if palindrom(number) else 'NO')
