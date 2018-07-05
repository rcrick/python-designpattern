# -*- coding: utf-8 -*-
import threading

try:
    from synchronize import make_synchronized
except ImportError:
    def make_synchronized(func):
        import threading
        func.__lock__ = threading.Lock()

        def sync_func(*args, **kws):
            with func.__lock__:
                return func(*args, **kws)

        return sync_func


class Singleton(object):
    instance = None

    @make_synchronized
    def __new__(cls, *args, **kws):
        if cls.instance == None:
            cls.instance = object.__new__(cls, *args, **kws)
        return cls.instance

    def __init(self):
        self.blog = 'xxx'

    def go(self):
        pass


def worker():
    s = Singleton()
    print id(s)
    s.go()


def test():
    e1 = Singleton()
    e2 = Singleton()
    e1.blog = 123
    print e1.blog
    print e2.blog
    print id(e1)
    print id(e2)


if __name__ == "__main__":
    test()
    task = []
    for one in range(30):
        t = threading.Thread(target=worker)
        task.append(t)

    for one in task:
        one.start()

    for one in task:
        one.join()
