# @time: 2022-10-15 15:45
# @author: 39295
import threading
import time


class A:
    b = 1


a = A()


def worker():
    a.b = 2


new_t = threading.Thread(target=worker, name='new thread')
new_t.start()
time.sleep(1)
print(a.b)