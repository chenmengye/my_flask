# @time: 2022-10-15 15:54
# @author: 39295
import threading,time
from werkzeug.local import Local


class A:
    b = 1


a = Local()
a.b = 1


def worker():
    a.b = 2
    print('in new thread b is:'+str(a.b))


new_t = threading.Thread(target=worker, name='new thread')
new_t.start()
time.sleep(1)
print('in main thread b is:'+str(a.b))