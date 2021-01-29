#coding=UTF-8
class Goods:
    def __init__(self, id, want, status, dname):
        self.id = id  # 商品编号
        self.want = want  # 期望价格
        self.status = status  # 运行状况
        self.dname = dname  # 商品名称
        self.name = None  # 商品名称
        self.price = None  # 当前价格
        self.date = None  # 记录日期
        self.url = 'https://item.jd.com/%s.html' % id  # 购买链接
        self.note = 0  # 通知备注

    def update(self, name, price, date):
        self.name = name
        self.price = price
        self.date = date

    def update_want(self, want):
        self.want = want

    def update_status(self, status):
        self.status = status

    def update_note(self, note):
        self.note = note
