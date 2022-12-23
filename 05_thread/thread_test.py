"""
主要编写的是进程和多线程

"""
from os import getpid
from random import randint
from threading import Thread
from time import sleep, time
from multiprocessing import Process

def download_task(file_name):
    print('开始下载', file_name)
    down_time = randint(5, 10)
    sleep(down_time)
    print('%s下载完成,耗时%d秒' % (file_name, down_time))


# 单线程模拟下载多本书籍
def single_thread_download_run():
    start = time()
    download_task('Python 从入门到精通.pdf')
    download_task('Java 从入门到精通.pdf')
    download_task('C++ 从入门到精通.pdf')
    print('全部下载完毕,耗时%.2f秒' % (time() - start))


################################################


# 多线程下载某本书籍
def download_thread_task(file_name):
    print('启用下载进程,进程号[%d].' % getpid())
    print('开始下载', file_name)
    down_time = randint(5, 10)
    sleep(down_time)
    print('%s下载完成,耗时%d秒' % (file_name, down_time))


# 多线程模拟下载多本书籍
def multi_thread_download_run():
    start = time()
    p1 = Process(target=download_thread_task, args=('Python 从入门到精通.pdf',))
    p1.start()
    p2 = Process(target=download_thread_task, args=('Java 从入门到精通.pdf',))
    p2.start()
    p3 = Process(target=download_thread_task, args=('C++ 从入门到精通.pdf',))
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print('Process线程 全部下载完毕,耗时%.2f秒' % (time() - start))


################################################

# 使用 threading线程下载
def multi_threading_download_run():
    start = time()
    t1 = Thread(target=download_thread_task, args=('Python 从入门到精通.pdf',))
    t1.start()
    t2 = Thread(target=download_thread_task, args=('Python 从入门到精通.pdf',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('threading线程 下载耗时%.3f秒' % (end - start))


################################################
class DownloadTask(Thread):

    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name

    def run(self):
        print('开始下载%s..' % self._file_name)
        time_download = randint(5, 10)
        sleep(time_download)
        print('%s下载完成! 耗费了%d秒' % (self._file_name, time_download))


# 创建自定义线程来模拟下载
def custom_threading_download_run():
    start = time()
    t1 = DownloadTask('Python 从入门到精通.pdf')
    t1.start()
    t2 = DownloadTask('Java 从入门到精通.pdf')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('自定义线程 下载耗时%.3f秒' % (end - start))


if __name__ == '__main__':
    # 单线程下载书籍
    # single_thread_download_run()
    # 多线程下载
    # multi_thread_download_run()
    # 多线程下载 2
    # multi_threading_download_run()
    # 创建自定义线程来模拟下载
    custom_threading_download_run()
