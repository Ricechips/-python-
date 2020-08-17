import requests
import parsel

url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E7%BA%A6%E4%BC%9A'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
response = requests.get(url, headers=headers)
# print(response)
html_data = response.text
html = parsel.Selector(html_data)
title_url = html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href').getall()
# print(title_url)

second_url = 'https://tieba.baidu.com'
for url in title_url:
    all_url = second_url + url
    print(all_url)

    response_2 = requests.get(url=all_url, headers=headers).text
    response_2_data = parsel.Selector(response_2)
    result_list = response_2_data.xpath('//cc/div/img[@class="BDE_Image"]/@src').getall()

    for li in result_list:
        img_data = requests.get(url=li, headers=headers).content
        file_name = li.split('/')[-1]
        with open('img\\' + file_name, mode='wb') as f:
            f.write(img_data)
            print('正在保存:', file_name)
