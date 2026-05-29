import random

print("=== 快递柜演示：同学们自己创建自己的柜子 ===\n")

def create_locker(item):
    # 外部函数：接收包裹物品，返回一个能凭码取件的内部函数
    # item 和 code 是外部函数的局部变量，正常情况下函数结束就销毁
    code = random.randint(100000, 999999)
    print(f"【快递员】放入 「{item}」，取件码已生成：{code}")

    def pickup(input_code):
        # 内部函数：记住了外部的 item 和 code，这就是闭包
        # 比较用户输入的取件码和闭包记住的取件码
        if str(input_code) == str(code):
            return f"取件码正确！取出了：【{item}】"
        else:
            return f"取件码错误！"

    return pickup
    # 返回内部函数，此时外部函数结束
    # 但 item 和 code 被内部函数引用，不会被销毁
    # 这就是闭包延长局部变量生命周期的原理


# ========== 第一步：同学们放包裹 ==========
# 每个同学调用 create_locker，生成一个独立的闭包

lockers = []
# 存储所有柜子信息，每个元素是 (姓名, 取件函数)

count = 3
# 人数，可以根据情况修改

for i in range(count):
    # 循环让每个同学操作一次
    name = input(f"第{i+1}位同学，你的名字是？")
    item = input(f"{name}，你想放什么东西进快递柜？")

    pickup_func = create_locker(item)
    # 调用 create_locker 生成闭包
    # 每次调用都会创建全新的 item 和 code，互不干扰
    # 这就是闭包工厂模式：同一个函数模板，生产多个独立的闭包实例

    lockers.append((name, pickup_func))
    # 只保存姓名和取件函数，不保存取件码
    # 取件码只存在于闭包内部，外面无法直接获取


print(f"\n====== 所有包裹已存放，共 {count} 个 ======\n")


# ========== 第二步：大家尝试取件 ==========
# 用户输入取件码，闭包负责验证

while True:
    # 无限循环，直到用户输入 q 退出
    input_code = input("请输入取件码（输入 q 退出）：")

    if input_code.lower() == "q":
        print("退出取件程序")
        break

    found = False
    # 标记是否找到匹配的柜子

    for name, pickup_func in lockers:
        # 遍历所有柜子，用每个闭包尝试验证
        result = pickup_func(input_code)
        # 即使 create_locker 早就执行完毕
        # 闭包内部的 code 和 item 仍然存活，可以正确比较

        if "正确" in result:
            # 匹配成功
            print(f"【{name}】的快递：{result}")
            found = True
            break
            # 一个码只对应一个柜子，找到就退出

    if not found:
        print(f"取件码 {input_code} 没有匹配任何柜子，再试试？")