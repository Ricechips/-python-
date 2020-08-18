import requests
import parsel

for page in range(1, 6):
    print('=====正在爬取第{}页数据====='.format(page))
    base_url = 'http://www.win4000.com/meinvtag26_{}.html'.format(page)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}


    response = requests.get(url=base_url, headers=headers)
    response.encoding = response.apparent_encoding
    html_data = response.text
    # print(html_data)

    parse = parsel.Selector(html_data)
    data_list = parse.xpath('//div[@class="Left_bar"]//ul/li/a/@href').getall()
    # print(data_list)
    # print(parse)

    for data in data_list:
        response_2 = requests.get(url=data, headers=headers).text

        html_2 = parsel.Selector(response_2)
        img_url = html_2.xpath('//div[@class="pic-meinv"]/a/img/@data-original').get()
        # print(img_url)

        img_data = requests.get(url=img_url, headers=headers).content

        file_name = img_url.split('/')[-1]
        # print(file_name)

        with open('cosplay\\' + file_name, mode='wb') as f:
            f.write(img_data)
            print('保存中: ', file_name)
