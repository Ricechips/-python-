import requests
import re

url = 'http://www.biquge.info/10_10582'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
    'Cookie': 'clickbids=10582; Hm_lvt_c979821d0eeb958aa7201d31a6991f34=1597723417; Hm_lvt_6dfe3c8f195b43b8e667a2a2e5936122=1597723938; Hm_lpvt_6dfe3c8f195b43b8e667a2a2e5936122=1597723938; Hm_lpvt_c979821d0eeb958aa7201d31a6991f34=1597723940'
}
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
html_data = response.text
# print(html_data)

result_list = re.findall('<dd><a href="(.*?)" title="(.*?)">.*</a></dd>', html_data)
print(result_list)

# for chapter_url, title in result_list:
#     try:
#         all_url = 'http://www.biquge.info/10_10582' + chapter_url
#         response_2 = requests.get(url=all_url, headers=headers)
#         response_2.encoding = 'utf-8'
#         html_data_2 = response_2.text
#         # print(html_data_2)
#
#         result = re.findall('<div id="content">(.*?)</div>', html_data_2, re.S)
#         if result:
#             with open('sancunrenjian\\' + title + '.txt', mode='w', encoding='utf-8') as f:
#                 f.write(result[0].replace('&nbsp;', "").replace('<br/>', "\n"))
#                 print('保存成功: ', title)
#     except Exception as e:
#         print(e)

