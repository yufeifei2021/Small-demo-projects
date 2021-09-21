"""
异步I/O操作 - asyncio模块
"""

import asyncio
import threading

# 用 asyncio 提供的 @asyncio.coroutine 
# 可以把一个generator标记为coroutine类型
# 然后在coroutine内部用 yield from 调用
# 另一个coroutine实现异步操作
@asyncio.coroutine
def hello():
    print('%s: hello, world!' % threading.current_thread())
    # 休眠不会阻塞主线程因为使用了异步I/O操作
    # 注意有yield from才会等待休眠操作执行完成
    yield from asyncio.sleep(2)
    print('%s: goodbye, world!' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
# 等待两个异步I/O操作执行结束
loop.run_until_complete(asyncio.wait(tasks))
print('game over!')
loop.close()
