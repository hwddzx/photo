import gevent
import requests
import time

start_time = time.time()


def f(url):
    print('GET: %s' % url)
    time.sleep(1)
    print('RES: %s' % url)


f('https://www.python.org/')
f('https://www.yahoo.com/')
f('https://www.baidu.com')
print(time.time() - start_time)
