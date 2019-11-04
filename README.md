使用Python，利用开源对分布式服务做协调。

在对分布式的应用做协调的时候，主要会碰到以下的应用场景：

- 业务发现（service discovery）
找到分布式系统中存在那些可用的服务和节点

- 名字服务 （name service）
通过给定的名字知道到对应的资源

- 配置管理 （configuration management）
如何在分布式的节点中共享配置文件，保证一致性。

- 故障发现和故障转移 （failure detection and failover）
当某一个节点出故障的时候，如何检测到并通知其它节点， 或者把想用的服务转移到其它的可用节点

- 领导选举（leader election）
如何在众多的节点中选举一个领导者，来协调所有的节点

- 分布式的锁 （distributed exclusive lock）
如何通过锁在分布式的服务中进行同步

- 消息和通知服务 （message queue and notification）
如何在分布式的服务中传递消息，以通知的形式对事件作出主动的响应

有许多的开源软件试图解决以上的全部或者部分问题，例如ZooKeeper，consul，doozerd等等，我们现在就看看它们是如何做的。