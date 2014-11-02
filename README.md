####文档
****
#####使用
&emsp;&emsp;使用MemCached()类实例化一个对象，例如：o = MemCached(addr,port)，addr是memcached服务器地址，port是服务器监听端口。
#####方法
######1.set(key, value)
&emsp;&emsp;存储数据，如果存在key覆盖，否则增加。
######2.add(key, data)
&emsp;&emsp;增加新key。
######3.replace(key, data)
&emsp;&emsp;替换数据。
######4.append(key, data)
&emsp;&emsp;增加数据在原数据之后。
######5.prepend(key, data)
&emsp;&emsp;增加数据在原数据之前。
######6.get(key)
&emsp;&emsp;获得数据。
######7.gets(key)
&emsp;&emsp;获得数据。
######8.delete(key)
&emsp;&emsp;删除数据。
######9.incr(key, number)
&emsp;&emsp;增加某一整数，默认为1
######10.decr(key, number)
&emsp;&emsp;减少某一整数，默认为1
######11.touch(key, exptime)
&emsp;&emsp;设置key过期时间。

