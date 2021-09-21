"""
生成器 - 使用yield关键字
"""
# 带有 yield 的函数不再是一个普通函数
# 而是一个生成器generator
# 可用于迭代，工作原理同上
# yield 是一个类似 return 的关键字
# 迭代一次遇到yield时就返回yield后面(右边)的值
def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        a, b = b, a + b
        n += 1

for x in fib(20):
    print(x)
