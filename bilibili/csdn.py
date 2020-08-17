import requests
import parsel

html = """<!doctype html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    {content}
</body>
</html>"""
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
}

response = requests.get('https://blog.csdn.net/qq_45096273/article/details/107902229?utm_medium=distribute.pc_feed.none-task-blog-personrec_hot-9.nonecase&depth_1-utm_source=distribute.pc_feed.none-task-blog-personrec_hot-9.nonecase&request_id=5f31e2e08c9fb674c6723c51', headers=headers)
# print(response.text)

selector = parsel.Selector(response.text)
article = selector.css('article').get()
print(article)

with open('csdn.html', mode='w', encoding='utf-8') as f:
    f.write(html.format(content=article))
