redis-cli启动redis
select 1 切换数据库
组成 str dict(hash) list sets sorted sets(有序集合)
是key value结构 每条数据都是键值对 键的类型为字符串 键不能重复
指令set get
setex key 设置过期时间，参考验证码过期。
ttl 查看key过期时间 类似验证码倒计时
![alt text](截图文件\image.png)
keys * 查看所有键
exists key 判断key是否存在
![alt text](截图文件\image-3.png)
type key 查看key类型
![alt text](截图文件\image-4.png)
mset key1 value1 key2 value2 批量设置key-value
例如 mset address "北京市海淀区" phone "13800138000"
![alt text](截图文件\image-1.png)
mget key1 key2 批量获取key-value
mget address phone
expire phone 10
![alt text](截图文件\image-2.png)
ttl phone 查看phone的过期时间
del key 删除key
![alt text](截图文件\image-5.png)
hash命令
hset person name itcast
hset person age 15
![alt text](截图文件\image-6.png)
hget person name
hget person age
![alt text](截图文件\image-7.png)
hmset person name itcast age 15 
![alt text](截图文件\image-8.png)
hmget person name age
hkeys person 查看person下所有键
![alt text](截图文件\image-9.png)
hvals person 查看person下所有值
![alt text](截图文件\image-10.png)
hdel person name 删除person下name键
![alt text](截图文件\image-11.png)
hset person age 20 更新person下age键的值
![alt text](截图文件\image-12.png)
list命令
lpush list1 a b c 向list1左侧插入元素
![alt text](截图文件\image-13.png)
顺序是推着走的
lrange list1 0 -1 取出list1所有元素  # 0是从头开始 -1是从最后一个开始
![alt text](截图文件\image-14.png)
# 类似浏览记录，最新浏览的在最前面
rpush list1 666  # 从右侧插入元素
lrange list1 0 -1
![alt text](截图文件\image-15.png)
lrem list1 0 a  # 删除list1第一个a元素 # 0代表全删除，1删一个，2删两个，-1代表从右边删除，-2删两个，-3删三个
![alt text](截图文件\image-16.png)
![alt text](截图文件\image-17.png)
![alt text](截图文件\image-18.png)
set命令
![alt text](截图文件\image-20.png)
sadd class china
sadd class usa
smembers class 取出class集合所有元素
![alt text](截图文件\image-21.png)
不重复，无顺序
srem class usa 移除class集合中的usa元素
![alt text](截图文件\image-22.png)
zset有序集合命令
zadd dashuju 100 zzx-100
![alt text](截图文件\image-23.png)
zrange dashuju 0 -1 取出dashuju集合所有元素 0是从头开始 -1是从最后一个开始
![alt text](截图文件\image-24.png)
pycharm 创建redis连接
![alt text](截图文件\image-25.png)
from redis import Redis
r = Redis(host='localhost', port=6379, db=0)
r.set('mingzi', 'itcast')
run
![alt text](截图文件\image-26.png)
1、导包 2、创建指令 3、执行指令 set、get、 delete
4、redis-cli 进入redis命令行 5、select 1 切换数据库 6、keys * 查看所有键 7、type key 查看key类型 8、mset key1 value1 key2 value2 批量设置key-value 9、mget key1 key2 批量获取key-value 10、expire key 10 设置过期时间 11、ttl key 查看key的过期时间 12、del key 删除key 13、hset key field value 设置hash 14、hget key field 获取hash 15、hmset key field1 value1 field2 value2 批量设置hash 16、hmget key field1 field2 批量获取hash 17、hkeys key 获取hash所有键 18、hvals key 获取hash所有值 19、hdel key field 删除hash 20、lpush key value
向list左侧插入元素 21、lrange key start stop 取出list所有元素 22、rpush key value 从右侧插入元素 23、lrem key count value 删除list元素 24、sadd key member 向set集合添加元素 25、smembers key 取出set集合所有元素 26、srem key member 移除set集合中的元素 27、zadd key score member 向有序集合添加元素 28、zrange key start stop 取出有序集合所有元素 29、zrem key member 移除有序集合中的元素 30、zrangebyscore key min max 取出有序集合中指定分数范围的元素 31、zremrangebyscore key min max 移除有序集合中指定分数范围的元素

