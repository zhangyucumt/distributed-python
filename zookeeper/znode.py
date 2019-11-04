# coding=utf-8
"""
对节点的基本操作 增删改查
"""
from kazoo.client import KazooClient, KazooState


zk = KazooClient(hosts='127.0.0.1:2181')

# 可以监听这个session的状态
def my_listener(state):
    if state == KazooState.LOST:
        print "session in lost state"
    elif state == KazooState.SUSPENDED:
        print "session in SUSPENDED state"
    else:
        print "session in connected state"


zk.add_listener(my_listener)


zk.start()

# ensure a path 不存在就创建
zk.ensure_path('/test/aa')

# 判断一个结点是不是存在
if zk.exists('/test/aa'):
    print "path /test/aa exists"
else:
    print "path /test/aa not exists"

zk.set('/test/aa', 'ccc')

#  创建一个含有数据的node
#  ephemeral 表示这是个临时节点 当会话断开的时候会删除
#  sequence  表示会创建一个带有后缀的节点
zk.create("/test/aa/node3", "a test value", sequence=True, ephemeral=True)

# 查询一个结点的version和data
data, stat = zk.get("/test/aa/node3")
print "Version: %s, data: %s" % (stat.version, data)

# 获取一个path的孩子
children = zk.get_children("/test/aa")
print "there are %s children, they are %s" % (len(children), children)

zk.stop()
