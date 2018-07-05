# -*- coding: utf-8 -*-
import threading

def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance


@singleton
class Highlander:
    x = 100
    # Of course you can have any attributes or methods you like.


def worker():
    hl = Highlander()
    hl.x += 1
    print hl
    print hl.x


def main():
    threads = []
    for _ in xrange(50):
        t = threading.Thread(target=worker)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
