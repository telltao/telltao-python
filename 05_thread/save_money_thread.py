from threading import Lock, Thread
from time import sleep


class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 获取锁 如果没有锁,那么执行的结果为 1
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 释放锁
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        # 你知道为什么当前类能执行 Account类的 deposit方法吗?
        # 因为在 thread_save_money 中 new了个 Account()对象,随后调用 AddMoneyThread 并传递了该对象,则就可以执行了
        self._account.deposit(self._money)


# 多线程模拟存钱
def thread_save_money():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为 %d元' % account.balance)


if __name__ == '__main__':
    thread_save_money()
