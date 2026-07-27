class Store:
    def __init__(self,s_name,s_num,s_price):
        self.s_name=s_name
        self.s_num=s_num
        self.s_price=s_price
        print("对象初始化完毕")
s1=Store("脉动",3,100)
print(s1.__dict__)