import re


# 验证qq号和数字是否符合标准
def verify_num():
    qq = input('请输入qq号')
    check = re.match(r'^[1-9]\d{4,11}$', qq)

    if not check:
        print('你的qq号码有误')
    else:
        print('你的qq号是对的')


# 替换不良内容
def replace_str():
    str = '你是干什么的,滚蛋,妈的智障'
    new_replace = re.sub('[妈的]|滚[蛋走狗]', '*', str, flags=re.IGNORECASE)
    print(new_replace)

# 拆分长字符串
def split_long_str():
    str = '浪里个浪,今天星期四.我欲乘风去,又恐琼楼玉宇,高处不胜寒'
    new_str_list = re.split(r'[,.]',str)
    while '' in new_str_list:
            new_str_list.remove('')
    print(new_str_list)

if __name__ == '__main__':
    # 验证qq号码是否正常
    # verify_num()
    # 过滤掉骂人的话
    # replace_str()
    split_long_str()
