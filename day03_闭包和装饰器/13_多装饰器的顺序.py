"""
需求：要创造多个装饰器当做力宏的衣服，装饰同一个原函数
步骤：
1.创建装饰器，创建4个，创建外部函数，传入一个函数，创建内部函数，
内部调用外部传入的函数，有返回在外部，有额外的功能
2.创建原函数
3.装饰同一个原函数
4.调用原函数
5.看看力宏被我们打扮成什么样了
"""

# 1.创建装饰器，创建4个，创建外部函数，传入一个函数，创建内部函数，
# 内部调用外部传入的函数，有返回在外部，有额外的功能
def leehom_naked():
    """基础状态：刚睡醒，赤裸的力宏"""
    return "🛌 赤裸的力宏"

def wear_underwear(function):
    """装饰器：穿内裤 (underwear = 内裤)"""
    def inner():
        return function() + " → 🩲 内裤"
    return inner

def wear_pants(function):
    """装饰器：穿外裤 (pants = 外裤)"""
    def inner():
        return function() + " → 👖 外裤"
    return inner

def wear_tshirt(function):
    """装饰器：穿T恤 (t-shirt = T恤)"""
    def inner():
        return function() + " → 👕 T恤"
    return inner

def wear_trenchcoat(function):
    """装饰器：穿风衣 (trench coat = 风衣)"""
    def inner():
        return function() + " → 🧥 风衣"
    return inner

# 2.创建原函数
# 3.装饰同一个原函数

# 错误的顺序
# @wear_underwear
# @wear_pants
# @wear_tshirt
# @wear_trenchcoat
# def lee_going_out():
#     """准备出门的力宏"""
#     return "🛌 赤裸的力宏"

# 正确的顺序
@wear_trenchcoat
@wear_tshirt
@wear_pants
@wear_underwear
def lee_going_out():
    """准备出门的力宏"""
    return "🛌 赤裸的力宏"


# 5.看看力宏被我们打扮成什么样了
print(lee_going_out())
