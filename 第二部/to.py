while True:
    usename=input("输入用户名")
    password=input("请输入密码")
    if usename==""or password=="":
        print("error")
    elif (usename=="admin"and password=="666888") or (usename=="zhangsan" and password=="123456"):
        print("登录成功")
        break
    else:
        print("用户名或密码错误")
