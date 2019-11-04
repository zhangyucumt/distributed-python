# coding=utf-8

from kazoo.client import KazooClient
import time
zk = KazooClient(hosts="127.0.0.1:2181")

zk.start()

@zk.DataWatch('/test/watch')
def my_func(data, stat):
    pass

time.sleep(10)

zk.stop()
