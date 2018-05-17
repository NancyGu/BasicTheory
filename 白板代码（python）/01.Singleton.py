# coding:utf-8
# python是天然单例模式
# python的某模块（文件）被另一个文件import的时候，在第一次加载编译生成pyc文件，之后直接调用pyc文件

# 第一种方法
# 文件：mysingleton.py
class Singleton(object):
    def foo(self):
        pass
my_singleton = Singleton()

# 文件：test.py
#from mysingleton import Singleton
my_singleton.foo()

# 第二种方法：装饰器
# 定义装饰器 Singleton1。
from functools import wraps
def Singleton1(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args,**kw)
        return instances[cls]
    return getinstance

@Singleton1
class Myclass(object):
    a = 1