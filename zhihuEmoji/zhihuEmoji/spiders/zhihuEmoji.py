'''
Function:
    知乎表情包爬取
Author:
    Charles
微信公众号:
    Charles的皮卡丘
'''
import re
import os
import scrapy
import requests
from fake_useragent import UserAgent
from zhihuEmoji.items import ZhihuemojiItem


'''知乎表情包爬取'''
class zhihuEmoji(scrapy.Spider):
    name = 'zhihuEmoji'
    allowed_domains = ['www.zhihu.com']
    question_id = '302378021'
    answer_url = 'https://www.zhihu.com/node/QuestionAnswerListV2'
    headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                'Accept-Encoding': 'gzip, deflate'
            }
    ua = UserAgent()
    '''请求函数'''
    def start_requests(self):
        offset = -10
        size = 10
        while True:
            offset += size
            data = {
                        'method': 'next',
                        'params': '{"url_token":%s,"page_size":%s,"offset":%s}' % (self.question_id, size, offset)
                    }
            self.headers['user-agent'] = self.ua.random
            yield scrapy.FormRequest(url=self.answer_url, formdata=data, callback=self.parse, headers=self.headers)
    '''解析函数'''
    def parse(self, response):
        # 用来保存图片
        if not os.path.exists(self.question_id):
            os.mkdir(self.question_id)
        # 解析响应获得问题回答中的数据, 然后获取每个回答中的图片链接并下载
        item = ZhihuemojiItem()
        answers = eval(response.text)['msg']
        imgregular = re.compile('data-original="(.*?)"', re.S)
        answerregular = re.compile('data-entry-url="\\\\/question\\\\/{question_id}\\\\/answer\\\\/(.*?)"'.format(question_id=self.question_id), re.S)
        for answer in answers:
            item['answer_id'] = re.findall(answerregular, answer)[0]
            image_url = []
            for each in re.findall(imgregular, answer):
                each = each.replace('\\', '')
                if each.endswith('r.jpg'):
                    image_url.append(each)
            image_url = list(set(image_url))
            for each in image_url:
                item['image_url'] = each
                self.headers['user-agent'] = self.ua.random
                self.download(requests.get(each, headers=self.headers, stream=True))
                yield item
    '''下载图片'''
    def download(self, response):
        if response.status_code == 200:
            image = response.content
            filepath = os.path.join(self.question_id, str(len(os.listdir(self.question_id)))+'.jpg')
            with open(filepath, 'wb') as f:
                f.write(image)