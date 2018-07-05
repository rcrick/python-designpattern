# -*- coding: utf-8 -*-

# 使用__new__


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self, status_number):
        self.status_number = status_number

s1 = Singleton(2)
s2 = Singleton(5)
print s1
print s2
print s1.status_number
print s2.status_number
#
# -------output-------
# <__main__.Singleton object at 0x7f7e2f776390>
# <__main__.Singleton object at 0x7f7e2f776390>
# 5
# 5
# -------output-------
#
# 使用装饰器
#
#
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kw):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kw)
        return _instance[cls]

    return _singleton


@Singleton
class MyClass(object):
    pass


print(MyClass() == MyClass())
