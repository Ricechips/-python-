import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
headers = {'User-Agent': ua}
r = requests.get('http://www.xiachufang.com/', headers=headers)
soup = BeautifulSoup(r.text)

img_list = []
for img in soup.select('img'):
    if img.has_attr('data-src'):
        img_list.append(img.attrs['data-src'])
    else:
        img_list.append(img.attrs['src'])

image_dir = os.path.join(os.curdir, 'images')
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

for img in img_list:
    o = urlparse(img)
    filename = o.path[1:].split('@')[0]
    filepath = os.path.join(image_dir, filename)
    url = '%s://%s/%s' % (o.scheme, o.netloc, filename)
    print(url)
    resp = requests.get(url)
    with open(filepath, 'wb') as f:
        for chunk in resp.iter_content(1024):
            f.write(chunk)

# 一行代码实现以上功能
# curl -s http://www.xiachufang.com/|grep -oP '(?<=src=\")http://i2\.chuimg\.com/\w+\.jpg'|xargs -i curl --create-dir {} -o ./images/{}
