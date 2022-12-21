"""
这是一个文件系统,从文件系统中读取文件
关于 open的描述
操作模式	具体含义
'r'	读取 （默认）
'w'	写入（会先截断之前的内容）
'x'	写入，如果文件已经存在会产生异常
'a'	追加，将内容写入到已有文件的末尾
'b'	二进制模式
't'	文本模式（默认）
'+'	更新（既可以读又可以写）

"""

# 读取文件的全部内容,然后输出
import os
import time
import json
import requests

def read_all_file():
    f = None
    # 增加了异常处理,对于程序代码更健壮
    try:
        f = open('test.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('指定的文件未找到')
    except LookupError:
        print('指定的编码格式有误')
    finally:
        if f:
            f.close()


# 按行循环读取文件
def read_line_file():
    with open('test.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()
    with open('test.txt', 'r', encoding='utf-8') as f:
        line = f.readline()
    # 按行读取,取第一行
    print(line)


# 写入文件 随机生成 1~10 如果是2的倍数,写到第一个文件里,否则写到第二个文件里
def write_all_file():
    filenames = ('test1.txt', 'test2.txt')
    fs_list = []
    try:
        for name in filenames:
            # 如果文件不存在则会直接新增
            fs_list.append(open(name, 'w', encoding='utf-8'))
        for number in range(1, 10):
            if number % 2 == 0:
                fs_list[0].write(str(number) + '\n')
            else:
                fs_list[1].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写入文件时发生错误')
    finally:
        for fs in fs_list:
            fs.close()
    print('文件全部写入成功')


# 读取二进制文件 通过读取第一个文件的二进制流,然后把文件写入到另一个文件里
def read_byte_file():
    try:
        with open('../3_gui_view/res/ball.jpeg', 'rb') as fs1:
            data = fs1.read()
            print('文件类型', type(data))
        with open('aa.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError:
        print('指定的文件未找到')
    except IOError as ex:
        print(ex)
        print('写入文件时发生错误')
    finally:
        fs1.close()
        fs2.close()
    print('读取二进制文件程序执行结束')


# 读写json文件
def read_write_json_file():
    json_arr = {
        "msg": "操作成功",
        "code": 200,
        "data": {
            "allCount": 1,
            "auditingCount": 1,
            "publishedCount": 0,
            "finishedCount": 0,
            "specialDownCount": 0,
            "loseEffectCount": 0
        },
        "tempstamp": 1671613334289
    }
    try:
        with open('data.json','w',encoding='utf-8') as fs:
            json.dump(json_arr,fs)
    except IOError as e:
        print(e)
    print('保存数据完成')


def get_news():
    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
    data_meta = json.loads(resp.text)
    print('返回数据',data_meta)
    for news in data_meta:
        print('得到的key',news)
    print('得到的msg', data_meta['msg'])


if __name__ == '__main__':
    # 读取全部文件内容
    # read_all_file()

    # 按行读取文件内容
    # read_line_file()

    # 写入文件
    # write_all_file()

    # 读写二进制文件
    # read_byte_file()

    # 读写json文件
    # read_write_json_file()
    # 爬取第三方网站,然后得到数据
    get_news()
