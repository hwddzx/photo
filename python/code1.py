from gevent import monkey
import gevent

monkey.patch_all()

import requests
import time

start_time = time.time()


def f(url):
    print('GET: %s' % url)
    time.sleep(1)
    print('RES: %s' % url)


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://www.baidu.com'),
])

print(time.time() - start_time)
