import requests
import pprint

sid = " "
cookie_response = requests.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=', headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
})
print(cookie_response.cookies)
for page in range(1, 31):
    if page % 5 == 0:
        cookie_response = requests.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=', headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        })
        print(cookie_response.cookies)
    headers = {
        "authority": "www.lagou.com",
        # "cookie": "JSESSIONID=ABAAABAABEIABCI7A9665674AC275D193D66C62D5A3CD46; Path=/; HttpOnly;SEARCH_ID=0a1196424c474928b7bd444d35ee84ac; Version=1; Max-Age=86400; Expires=Sat, 15-Aug-2020 09:56:50 GMT; Path=/;user_trace_token=20200814175650-0a6d706e-3cb8-4157-9792-2f566be77165; Max-Age=31536000; Path=/; Domain=.lagou.com;X_HTTP_TOKEN=42daf4b72327b2810109937951bf5e71415983ed09; Max-Age=31536000; Path=/; Domain=.lagou.com;",
        "origin": "https://www.lagou.com",
        "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
    }
    if page == 1:
        data = {
            'first': 'true',
            'pn': '1',
            'kd': 'python'
        }
    else:
        data = {
            'first': 'false',
            'pn': str(page),
            'kd': 'python',
            'sid': sid
        }


    api_url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    response = requests.post(api_url, headers=headers, cookies=cookie_response.cookies)
    # pprint.pprint(response.json())
    # print(response.text)
    data = response.json()
    result = data['content']['positionResult']['result']
    sid = data['content']['showId']
    for r in result:
        d = {
            'city': r['city'],
            'companyFullName': r['companyFullName'],
            'companySize': r['companySize'],
            'education': r['education'],
            'positionName': r['positionName'],
            'salary': r['salary'],
            'workYear': r['workYear'],
        }
        print(d)
    with open('lagou.csv', mode='a', encoding='utf-8-sig') as f:
        f.write(",".join(list(d.values())))
        f.write('\n')
