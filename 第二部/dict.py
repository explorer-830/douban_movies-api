
market={}
print("######欢迎来到自助商城######")
print("#     1.添加购物车     #")
print("#     2.修改购物车     #")
print("#     3.删除购物车     #")
print("#     4.查询购物车     #")
print("5.exit")

while True:
    choose = input("请输入你的选择")
    match choose:
        case "1":
            good_name=input("输入你所挑选的商品")
            good_num=input("输入商品的数量")
            price=input("输入商品的价格")
            if good_name in market.keys():
                print("error")
            elif good_name not in market.keys():
                 market[good_name]={"商品数量":good_num,"商品价格":price}
        case "2":
            good_name = input("输入你所挑选的商品")
            good_num = input("输入商品的数量")
            price = input("输入商品的价格")
        case "3":
            good_name=input("输入需要删除的商品")
            if good_name not in market.keys():
                print("error")
            else:
                del market[good_name]
        case "4":
            for i in market.keys():
                good_info=market[i]
                print(f"商品名称：{i}以及商品信息：{good_info}")
        case "5":
            break
        case _:
            print("error")