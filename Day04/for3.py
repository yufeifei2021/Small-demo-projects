"""
输入非负整数n计算n!
"""

n = int(input('n = '))
result = 1
for x in range(1, n + 1): # n+1是开区间 取不到
    result *= x
print('%d! = %d' % (n, result))
