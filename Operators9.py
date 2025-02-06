print(5 == 4 + 1)
"""
The "like" comparison has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 5 == 5 = True
"""
print(not 5 == 5)
"""
The logical NOT operator has a lower precedence than "like" comparison, and we need to calculate the comparison first.
The calculation above reads: not True = False
"""
print(1 or 2 and 3)
"""
The and operator has a higher precedence than or, and we need to calculate the and expression first.
The calculation above reads: 1 or 3 = 1
"""
print(4 or 5 + 10 or 8)
"""
The or operator has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads: 4 or 15 or 8 = 4
"""
print(5 + 4 - 7 + 3)
"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""