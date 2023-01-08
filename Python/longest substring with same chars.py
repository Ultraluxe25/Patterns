"""
Дана строка s. Найдите в ней подстроку, где наибольшее количество подряд идущих одинаковых символов. Выведите символ и длину последовательности.
Если таких несколько – выведите последнюю.

Ввод:

s – строка

Вывод:

res – символ последовательности

acc – длина самой большой последовательности

Sample Input:
aaabbccccaaaab

Sample Output:
a
4
"""

def find_longest_substring(text):
    longest = ''
    current_substring = ''
    text += ' '
    
    if len(text) == 1:
        return text, 1
    
    for index, value in enumerate(text):
        if value not in current_substring and len(longest) <= len(current_substring):
            longest = current_substring
            current_substring = value
        elif value not in current_substring:
            current_substring = value
        else:
            current_substring += value
                    
    return longest[0], len(longest)


s = input()
res, acc = find_longest_substring(s)
print(res, acc, sep='\n')
