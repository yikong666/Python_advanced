#  编写 `counter()`，外层定义 `count = 0`。
#  内层函数每调用一次 `count + 1` 并返回新值。
#  必须使用 `nonlocal`，并连续调用至少 3 次验证状态被保存。



#  编写 `counter()`，外层定义 `count = 0`。
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

c1 = counter()
print(c1(),'第一次')
print(c1(),'第二次')
print(c1(),'第三次')

