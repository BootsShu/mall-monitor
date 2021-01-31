#coding=UTF-8
import configparser
import requests
import json

class Dingding:
    def __init__(self, config='config.cfg'):
        cfg = configparser.ConfigParser()
        cfg.read(config)
        self.webhook = cfg.get('dingding', 'webhook')
        self.header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }

    def send(self, name, price, want, url):
        text = '降价啦！商品名称：%s\n目前价格：%.2f\n期望价格：%.2f\n购买链接：%s' % (name, price, want, url)
        try:
            message_json = json.dumps({
                "msgtype": "text",
                "text": {
                    "content": text
                },
                "at": {
                    "isAtAll": True
                }
            })
            info = requests.post(url=self.webhook,data=message_json,headers=self.header)
            print('发送成功')
            print(info.text)
        except smtplib.SMTPException:
            print('发送失败')


if __name__ == '__main__':
    ding = Dingding()
    ding.send('金士顿(Kingston) 240GB SSD固态硬盘 SATA3.0接口 A400系列',
              219.00, 219.00, 'https://item.jd.com/4311178.html')
