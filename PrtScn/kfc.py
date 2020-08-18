import requests
import pprint
import csv

for page in range(1, 11):
    print('======第{}页======'.format(page))
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

    data = {
        'cname': '',
        'pid': '',
        'keyword': '杭州',
        'pageIndex': str(page),
        'pageSize': '10'
    }

    response = requests.post(url=base_url, data=data, headers=headers)
    json_data = response.json()
    # pprint.pprint(json_data)

    json_list = json_data['Table1']
    # print(json_list)

    for json_1 in json_list:
        storeName = json_1['storeName'] + '餐厅'
        provinceName = json_1['provinceName']
        addressDetail = json_1['addressDetail']
        pro = json_1['pro']
        print(storeName, provinceName, addressDetail, pro, sep='|')

        with open('kfc.csv', mode='a', newline="") as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow([storeName, provinceName, addressDetail, pro])
