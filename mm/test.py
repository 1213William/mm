import requests

headers = {
    # 'user-agent': UserAgent(verify_ssl=False).chrome
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'UM_distinctid=16d68e3ebfe32b-0c81530cf904fc-38607701-1aeaa0-16d68e3ebff7bd; Hm_lvt_672e68bf7e214b45f4790840981cdf99=1569422830,1569507842; Hm_lpvt_672e68bf7e214b45f4790840981cdf99=1569544030; CNZZDATA1277874215=1602513911-1569420044-%7C1569538896',
    'pragma': 'no-cache',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Referer': 'https://www.mm131.net'
}


with open('aaa.png', 'wb') as fp:
    fp.write(requests.get('https://img1.mmmw.net/pic/5123/20.jpg', headers=headers).content)
    print(111)

"""
https://images.weserv.nl/?url=https://img1.mmmw.net/pic/5132/8.jpg
"""


