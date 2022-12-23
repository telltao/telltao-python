"""
调用数据网站下载图片

"""
from os import getpid
from random import randint
from threading import Thread
from time import sleep, time
from multiprocessing import Process

import requests


class DownloadData(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        file_name = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        save_url = './images/' + file_name
        with open(save_url, 'wb') as f:
            f.write(resp.content)
            print('文件写入完成,文件名:', save_url)


def thread_download_data():
    # 申请你的 key https://www.tianapi.com/gethttp/67 然后把你的key放到下面这个url里即可
    key = 'key'
    resp = requests.get('https://apis.tianapi.com/htmlpic/index?key=' + key + '&url=https://www.tianapi.com/article/62')
    json = resp.json()
    print('调用接口返回数据为', json)
    try:
        for dict in json['result']['list']:
            url = dict['picUrl']
            DownloadData(url).start()
    except KeyError as e:
        print('调用接口发生了错误,异常原因', e)


if __name__ == '__main__':
    # 创建自定义线程然后下载图片
    thread_download_data()
