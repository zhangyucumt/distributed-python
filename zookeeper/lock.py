# coding=utf-8
"""
分布式锁
"""

from kazoo.client import KazooClient
import time
from uuid import uuid4

my_id = uuid4()
zk = KazooClient(hosts="127.0.0.1:2181")

zk.start()

lock = zk.Lock("/test/lock", my_id)

def work():
    print "i am %s" % uuid4

while True:
    with lock:
        work()
    time.sleep(3)

zk.stop()