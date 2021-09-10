"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3
"""

for num in range(100, 1000): # 100~999
    low = num % 10 # 百位
    mid = num // 10 % 10 # 十位
    high = num // 100 # 个位
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
