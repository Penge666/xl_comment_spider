import requests
import re
import os
from time import sleep
from PIL import Image
from wordcloud import WordCloud
import jieba
import numpy as np
B=0
def catch_page():
        global B
        A='https://m.weibo.cn/comments/hotflow?id=4626660639379459&mid=4626660639379459&max_id='
        C='&max_id_type='
        D=0
        headers = {
            'Cookie': 'WEIBOCN_FROM=1110006030; __guid=52195957.2638991681126455000.1618631177945.1882; loginScene=102003; SUB=_2A25NfitvDeRhGeNI7VcQ9CjFwzSIHXVugLUnrDV6PUJbkdAfLXnEkW1NSFGqFA8ZkYMw6iufthEQqJdSfQJJE73b; _T_WM=32428089373; XSRF-TOKEN=14a676; MLOGIN=1; monitor_count=6; M_WEIBOCN_PARAMS=oid%3D4626705668640610%26luicode%3D20000061%26lfid%3D4626705668640610%26uicode%3D20000061%26fid%3D4626705668640610',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'
        }
        # furl = 'https://m.weibo.cn/comments/hotflow?id=4626660639379459&mid=4626660639379459&max_id_type=0'
        # first = requests.get(url=furl,headers=headers)
        # B=first.json()['data']['max_id']
        # print(first.content)
        # 数据解析
        name_list, content_list, all_list = [],[],None
        for i in range(0, 10):
            url=str(A)+str(B)+str(C)+str(D)
            print(url)
            #print(url)
            res = requests.get(url=url, headers=headers)
            sleep(3)
            print(res.content)

            # print(max_id)
            B = res.json()['data']['max_id']
            if(i>14):
                D=1
            # print(max_id)
            #print(res.json()['data']['max_id'])
            l = len(res.json()['data']['data'])
            #print(l)
            for k in range(0, l):
                content_list.append(res.json()['data']['data'][k]['text'])
            #    print(res.json()['data']['data'][k]['text'])
            ll = len(content_list)
            # print(ll)
            for i in range(0, ll):
                content_list[i] = re.sub('<.*?>', '', content_list[i])
                print(content_list[i])
                with open('E:\\Lab\\词云\\text.txt', "a", encoding="utf8") as a:
                    a.write(content_list[i] + '\n')
def make_photo():
    # 1:打开词云文本
    txt = open("E:\\Lab\\词云\\text.txt", "rb").read()
    # 2:用jieba进行分词
    txtout = "".join(jieba.cut(txt, cut_all=False))
    # 3:读取词云图片
    mask_pic = Image.open("E:\\Lab\\词云\\task.png")
    mask_pic_array = np.array(mask_pic)  # 将词云图片转换为数组
    # 4:设置词云的属性
    font = "C:\\Windows\\Fonts\\STXINGKA.TTF"  # 词云的中文字体所在路径
    wc = WordCloud(font_path=font,
                   background_color="white",
                   mask=mask_pic_array,
                   contour_width=5,
                   contour_color="lightblue",
                   )
    # 5:生成词云
    wc.generate(txtout)
    # 6:存储词云
    wc.to_file("E:\\Lab\\词云\\photo.png")
if __name__ == '__main__':
    # catch_page()
    make_photo()