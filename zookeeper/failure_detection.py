# coding=utf-8
"""
故障检测 
通过创建 ephemeral node 来进行故障检测
"""
import time
import sys
from kazoo.client import KazooClient, KazooState


zk = KazooClient(hosts='127.0.0.1:2181')

def node():
    zk.start()
    zk.ensure_path("/test/failure_detection")
    zk.create(path="/test/failure_detection/node", value="aaa", ephemeral=True)
    time.sleep(15)
    zk.stop()

def check():
    zk.start()
    while True:
        if zk.exists("/test/failure_detection/node"):
            print "node is alive"
        else:
            print "node is dead"
            break
        time.sleep(1)
    zk.stop()


if __name__ == '__main__':
    action = sys.argv[1]
    if action == 'node':
        node()
    else:
        check()
    