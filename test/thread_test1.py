# @time: 2022-10-15 15:19
# @author: 39295
import threading
import time

'''线程之间的先后执行顺序'''


def worker():
    print('123')
    t = threading.current_thread()
    time.sleep(10)
    print(t.getName())


new_t = threading.Thread(target=worker, name='new_thread')
new_t.start()

t = threading.current_thread()
print(t.getName())