# coding=utf-8
"""
Zookeeper 使用树形目录作为数据模型。这个目录和文件结构类似，目录上的每个结点称为 ZNodes
Zookeeper 提供API来操作这些 znodes 包括增删改查等
zookeeper 还提供一些 recipe  来实现锁 两阶段提交 领导选举等
"""
