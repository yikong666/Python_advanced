# ==========================================
# 核心口诀：带参数的装饰器，就是“三层俄罗斯套娃”
# outer (外层) -> 负责接收“参数”
# middle(中层) -> 负责接收“原函数”
# inner (内层) -> 负责实际“干活”
# ==========================================

def outer(topping_name, sugar_level="正常糖"):
    """
    【第 1 层】外层：负责记住参数
    """

    def middle(func):
        """
        【第 2 层】中层：负责接管原来的函数
        """

        def inner(*args, **kwargs):
            """
            【第 3 层】内层：真正执行的包装动作
            """
            print(f"👉 [看小票] 顾客要求：加【{topping_name}】，甜度【{sugar_level}】")
            print(f"👉 [第一步] 往空杯子里，加入满满的 {topping_name}...")

            # 调用原来的函数，做基础的茶底
            result = func(*args, **kwargs)

            print(f"👉 [最后一步] 封口，贴上【{sugar_level}】的标签，出餐！")
            return result

        return inner  # 中层把内层交出去

    return middle  # 外层把中层交出去


# ==========================================
# 下面开始模拟点单（使用语法糖 @）
# ==========================================

@outer(topping_name="黑糖珍珠", sugar_level="三分糖")
def make_milk_tea():
    print("   [做茶底] 倒入红茶，加入牛奶，疯狂摇匀...")
    return "经典奶茶"


@outer(topping_name="厚芋泥", sugar_level="无糖")
def make_coconut_water():
    print("   [做茶底] 砸开新鲜椰子，倒入清甜椰子水...")
    return "生椰水"

@outer(topping_name="柠檬", sugar_level="五分糖")
def make_coconut_water():
    print("   [做茶底] 加入矿泉水,加入红茶基茶,倒入半杯冰块 ...")
    return "柠檬红茶"

# ==========================================
# 测试调用
# ==========================================
if __name__ == '__main__':
    # print("--- 🔔 叮咚！顾客 A 的外卖订单 ---")
    # drink1 = make_milk_tea()
    # print(f"✅ 顾客 A 拿到了：{drink1}\n")
    #
    # print("--- 🔔 叮咚！顾客 B 的外卖订单 ---")
    # drink2 = make_coconut_water()
    # print(f"✅ 顾客 B 拿到了：{drink2}")

    print("--- 🔔 叮咚！顾客 brianwang 的外卖订单 ---")
    drink3 = make_coconut_water()
    print(f"✅ 顾客 B 拿到了：{drink3}")