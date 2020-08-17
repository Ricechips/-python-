import requests
import re
import csv
import jieba
import wordcloud
import imageio

# url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=225087170'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
#     "cookie": "_uuid=5AA69F50-38EF-8FFC-7C01-B4F99B050FD502894infoc; buvid3=38E51733-216E-4055-9EEA-3956E4B3FB48143086infoc; sid=4m4jia0c; DedeUserID=98393989; DedeUserID__ckMd5=03355284927a19a3; SESSDATA=42f81165%2C1613187850%2C8409c*81; bili_jct=7c2cfef549ada445c0f322defe422730; CURRENT_FNVAL=16; bfe_id=c5d4c382b0a326b5f45ec37e1aea9efa; rpdid=|(JR)kYYR))0J'ulm~YJl)~Y"
# }
# resp = requests.get(url, headers=headers)
# html_doc = resp.content.decode('utf-8')
# res = re.compile('<d.*?>(.*?)</d>')
# danmu = re.findall(res,html_doc)
# print(danmu)
#
# for i in danmu:
#     with open('C:/Users/aoc/PycharmProjects/pythonProject/danmu.csv','a',newline='',encoding='utf-8-sig') as f:
#             writer = csv.writer(f)
#             danmu = []
#             danmu.append(i)
#             writer.writerow(danmu)

f = open('C:/Users/aoc/PycharmProjects/pythonProject/danmu.csv',encoding='utf-8')
txt = f.read()
txt_list = jieba.lcut(txt)
print(txt_list)
string = "".join(txt_list)
print(string)

mk = imageio.imread(r'C:/Users/aoc/PycharmProjects/pythonProject/bilibili.png')
print(mk)
w = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color='white',
    font_path="msyh.ttc",
    stopwords={" "},
    mask=mk,
    contour_width=5,
    contour_color='red'
)

w.generate(string)
w.to_file('C:/Users/aoc/PycharmProjects/pythonProject/output1.png')
