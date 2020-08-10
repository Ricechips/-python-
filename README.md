# python3.8+pycharm2020.2+mysql8.0.21

## python
https://www.python.org/downloads/windows/

## pycharm
https://www.jetbrains.com/pycharm/download/#section=windows<br>
Professional激活方法<br>
Community版本没有内置database插件,并且最新版没有可用的插件

## mysql
https://dev.mysql.com/downloads/<br>
创建my.ini配置文件
```c
[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8
 
[mysqld]
# 设置3306端口
port = 3306
# 设置mysql的安装目录
basedir=C:\MySQL\mysql-8.0.15
# 设置 mysql数据库的数据的存放目录，MySQL 8+ 不需要以下配置，系统自己生成即可，否则有可能报错
# datadir=C:\\web\\sqldata
# 允许最大连接数
max_connections=20
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
```
C:\Windows\system32>cd C:\mysql\mysql-8.0.21-winx64\bin<br>
.\mysqld --initialize --console<br>
.\mysqld install<br>
net start mysql<br>
C:\mysql\mysql-8.0.21-winx64\bin>mysql -u root -p<br>
alter user user() identified by 'ricechips';

## abaaba
壁纸https://wallhaven.cc/<br><br>
报错解决<br>
Q:由于找不到msvcp140.dll无法继续执行代码<br>
A:下载https://www.microsoft.com/zh-cn/download/confirmation.aspx?id=48145<br><br>
Q:服务没有响应控制功能<br>
A:C:\mysql\mysql-8.0.21-winx64\bin>mysqld --console<br><br>
Q:装scrapy,Microsoft Visual C++ 14.0 is required.<br>
A:https://visualstudio.microsoft.com/zh-hans/visual-cpp-build-tools/<br><br>
Q:Cannot open include file: 'basetsd.h': No such file or directory<br>
A:https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk/<br><br>
Q:fatal error LNK1158: cannot run 'rc.exe'<br>
A:在环境变量path中添加C:\Program Files (x86)\Windows Kits\10\bin\10.0.19041.0\x64<br>
将rc.exe和rcdll.dll<br>从C:\Program Files (x86)\Windows Kits\10\bin\10.0.19041.0\x64复制到C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin<br><br>
![avatar]()
