import requests
import json


def spiderTaoBao():
    url = "https://rate.tmall.com/list_detail_rate.htm"
    header = {
        # 替换成自己的
        "cookie": "",
        "referer": "https://detail.tmall.com/item.htm",
        # 替换成自己的
        "user-agent": "",
    }
    params = {  # 必带信息
        "itemId": "39488472991",  # 商品id
        "sellerId": "2064892827",
        "currentPage": "1",  # 页码
        "callback": "jsonp873",
    }
    req = requests.get(url, params, headers=header)
    content = req.content.decode('utf-8')[11:-1];  # 解码，并且去除str中影响json转换的字符jsonp873;
    result = json.loads(content);
    print(result['rateDetail']['rateList'][1]['rateContent'])


if __name__ == '__main__':
    spiderTaoBao()
