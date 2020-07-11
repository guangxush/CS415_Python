import requests
import json
import time
import random


class TaoBao:
    lastPage = 99
    url = "https://rate.tmall.com/list_detail_rate.htm"
    header = {
        "cookie": "",
        "referer": "https://detail.tmall.com/item.htm",
        "user-agent": "",
    }
    params = {  # 必带信息
        "itemId": "0",  # 商品id
        "sellerId": "2064892827",
        "currentPage": "1",  # 页码
        "callback": "jsonp873",
    }

    def __init__(self, id: str):
        self.params['itemId'] = id

    def getPageData(self, pageIndex: int):
        self.params["currentPage"] = str(pageIndex)
        req = requests.get(self.url, self.params, headers=self.header, timeout=2).content.decode(
            'utf-8');  # 解码，并且去除str中影响json转换的字符（\n\rjsonp(...)）;
        req = req[req.find('{'):req.rfind('}') + 1]
        return json.loads(req)

    def setOrder(self, way: int):
        self.params["order"] = way;

    def getAllData(self):
        rateDataList = []
        for i in range(0, self.lastPage + 1):
            time.sleep(random.random() * 3)  # 随机睡眠n秒，模拟人的行为
            pageDate = self.getPageData(i)['rateDetail']['rateList']
            for j in range(0, 20):
                rateDataList.append(pageDate[j]['rateContent'])
                print(pageDate[j]['rateContent'])
        return rateDataList


if __name__ == '__main__':
    taobao = TaoBao("39488472991")
    rateDataList = taobao.getAllData()
    for data in rateDataList:
        print(data)
