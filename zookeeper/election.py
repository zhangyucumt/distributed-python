# coding=utf-8
"""
领导选举
当leader被杀死之后从worker中会被选举出来一个新的leader
"""

from kazoo.client import KazooClient
from uuid import uuid4
import time
import sys

my_id = uuid4()

def leader_func():
    print "%s is leader" % my_id
    while True:
        print "%s is working" % my_id
        time.sleep(3)

zk = KazooClient(hosts="127.0.0.1:2181")
zk.start()

election = zk.Election("/test/election")

# 会一直阻塞 直到被选举称为leader
election.run(leader_func)

zk.stop()
