import requests
import parsel

for page in range(3, 3534):
    print('========第{}页========'.format(page))
    base_url = 'https://www.doutula.com/photo/list/?page={}'.format(str(page))
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

    response = requests.get(url=base_url, headers=headers)
    html_data = response.text
    # print(html_data)

    selector = parsel.Selector(html_data)
    # print(selector)
    result_list = selector.xpath('//a[@class="col-xs-6 col-sm-3"]')

    for result in result_list:
        title = result.xpath('./img/@alt').get()
        img_url = result.xpath('./img/@data-original').get()

        all_title = title + "." + img_url.split('.')[-1]
        # print(all_title)

        img_data = requests.get(url=img_url, headers=headers).content

        with open('img\\' + all_title, mode='wb') as f:
            f.write(img_data)
            print('保存完成:', all_title)
