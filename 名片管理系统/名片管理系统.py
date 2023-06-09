dicName = {'张三':['男',13312344321,'zhangsan@cueb.edu.cn','zhangsan'],
           '李四':['男',12356788765,'lisi@cueb.edu.cn','lisi8765']}


cards = [{
    "name": "张三",
    "gender":"男",
    'phone':'13312344321',
    "Email": "zhangsan@cueb.edu.cn",
    "wechat": "zhangsan",
}, {
    "name": "李四",
    "gender":"男",
    "phone":"12356788765",
    "Email": "lisi@cueb.edu.cn",
    "wechat": "lisi8765",
}]  # 定义一个的列表用于存放名片信息，默认里面有张三和李四的信息，方便以后调试用。



def print_menu():
    """"完成打印功能菜单"""
    print("=" * 20)
    print("    名片管理系统")
    print(" 1:添加一个名片")
    print(" 2:删除一个名片")
    print(" 3:修改一个名片")
    print(" 4:查询一个名片")
    print(" 5:退出")
    print("=" * 20)
    
    
def add_card():
    """完成添加一个名片的功能"""
    new_infor: dict = {
        "name": input("请输入名字："),
        "gender": input("请输入性别："),
        "phone": input("请输入电话："), 
        "Email": input("请输入邮箱："), 
        "wechat": input("请输入微信：")
    }
    cards.append(new_infor)
    print("添加成功！")
    
def delete_card():
    del_name = input("请输入要删除的名字：")
    for person in cards:
        if del_name == person["name"]:
            cards.remove(person)
            print("删除成功！")
            break
    else:
        print("名片管理系统中无此人")    
    
def update_card():
    name: str = input("请输入要修改的名字：")
    for person in cards:
        if name == person["name"]:
            phone = input("请输入新的的电话：")
            Email = input("请输入新的的邮箱：")
            wechat = input("请输入新的的微信：")
            if phone:
                person["phone"] = phone
            if Email:
                person["Email"] = Email
            if wechat:
                person["wechat"] = wechat
            print("修改成功")
            break
    else:
        print("找不到要修改的人！")    
    
def find_card():
    find_name: str = input("请输入要查询的名字：") 
    flag: int = 1
    for temp in cards:
        # 遍历名片中的所有名字，判断要查找的名字是否存在，不存在则打印查无此人
        if temp["name"].find(find_name) != -1:
            print("%s\t%s\t%s\t%s\t%s" % (temp["name"], temp["gender"], temp["phone"], temp["Email"], temp["wechat"]))
            flag = 0
    if flag:
        print("查无此人")    
    
    
print_menu()
while True:
    num: str = input("请输入功能序号：")
    if not num.isdigit():
        print("请输入数字！")
        continue
    num: int = int(num)
    if num == 1:
        add_card()
    elif num == 2:
        delete_card()
    elif num == 3:
        update_card()
    elif num == 4:
        find_card()
    elif num == 5:
        break
    else:
        print("请按号输入！")
    print()
    
    
    
    
    
    
    
    
    
    
    
    
    
