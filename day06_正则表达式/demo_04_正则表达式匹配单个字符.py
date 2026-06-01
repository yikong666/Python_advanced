r"""
需求：查看正则表达式匹配单个字符的每一个形式
包括：.  []  [^] \d \D
使用正则匹配表达式去匹配
查看结果


步骤：
1.导包
2.编写正则匹配和表达式
3.打印结果并观察总结
"""

# 1.导包
import re


# 打印的方法
# 【优化】定义提取函数，增加 pattern(正则), text(文本), desc(规则描述) 参数
def get_data(result, pattern, text, desc):
    print(f"▶ 正在测试: {desc}")
    print(f"  ├─ 正则表达式: r'{pattern}'")
    # repr() 可以让 \n \t 等不可见字符原样显示出来，方便观察
    # 为了直观看到文本中的换行和制表符，我们用 repr() 打印原样字符串
    print(f"  ├─ 目标文本:   {repr(text)}")
    if result:
        print(f"  └─ ✅ 匹配成功: '{result.group()}'\n")
    else:
        print(f"  └─ ❌ 匹配失败\n")


print('==================== 1. 匹配任意字符 (.) ====================')
#  1
# . : 匹配任意1个字符(除了\n)
# 【做了什么】用 8个点 匹配目标字符串的前 8个字符。
# 【为什么】'bz666_黑马' 刚好是8个字符（Python3中，汉字也算作一个字符）。
# parrten1, text1 = r"........", "bz666_黑马"
# result = re.match(pattern=parrten1, string=text1)
# get_data(result, parrten1, text1, "用'.'来匹配任意字符串（除了换行符）")


#  2
# 【做了什么】尝试用 . 去匹配换行符 \n。
# 【为什么失败】因为 . 的底层规则是“除了换行符以外的任意字符”。
# 【之后怎么做】如果遇到多行文本，需要传 re.S 参数。
# parrten2, text2 = r".", "\n"
# result = re.match(pattern=parrten2, string=text2)
# get_data(result, parrten2, text2, "用'.'来匹配换行符")


#  3
# # [x] : 匹配括号中任意1个字符
# # 【做了什么】定义了3个字符位：[字母/数字/下划线] + [纯数字] + [字母/数字/下划线]。
# # 【为什么】'b6_' 完全符合这三个坑位的要求。
# parrten3, text3 = r"[a-zA-Z0-9][0-9][a-zA-Z0-9_!]", "21!"
# result = re.match(pattern=parrten3, string=text3)
# get_data(result,parrten3,text3,"用[x]来匹配括号中任意一个符合条件的字符")


#  4
# # [^x]:匹配除了x外的所有字符
# parrten4, text4 = r"[^a][^a][^a]", "b2#"
# result = re.match(pattern=parrten4, string=text4)
# get_data(result,parrten4,text4,"用[^x]来匹配不为括号中元素的字符")


#  5
# # 【为什么失败】目标字符串就是 'a'，但正则要求“不能是a”。
# pattern5, text5 = r'[^a]', 'a'
# result = re.match(pattern5, text5)
# get_data(result, pattern5, text5, "'[^x]' 文本本身就是a(预期失败)")


#  6
# # \d匹配数字
# parrten6, text6 = r"bz\d\d\d_黑马", "bz357_黑马"
# result = re.match(pattern=parrten6, string=text6)
# get_data(result, parrten6, text6, "用\d来匹配当前位置为数字的字符,且前边位置的字符也要符合")


#  7
# # \D匹配非数字
# parrten6, text6 = r"\D", "s"
# result = re.match(pattern=parrten6, string=text6)
# get_data(result,parrten6,text6,"用\D来匹配当前位置不为数字的字符")


#  8
# # \s匹配空白
# parrten8, text8 = r"bz\s666\s黑马\s", "bz 666 黑马\n"
# result = re.match(pattern=parrten8, string=text8)
# get_data(result,parrten8,text8,r"用\s来匹配空格")


#  9
# # \S匹配非空白
# parrten9, text9 = r"\S", " \t\n"
# result = re.search(pattern=parrten9, string=text9)
# get_data(result,parrten9,text9,r"用\S来匹配非空格")


#  10
# # 匹配\w非特殊字符a-zA-Z0-9_汉字
# parrten10, text10 = r"\w\w\w\w\w\w\w\w", "bz357_黑马"
# result = re.search(pattern=parrten10, string=text10)
# get_data(result,parrten10,text10,r"用\w来匹配非特殊字符")


#  11
# # 匹配\W特殊字符 非a-zA-Z0-9_汉字，例如#￥$%^&*
parrten11, text11 = r"\W\W\W", "!@#"
result = re.search(pattern=parrten11, string=text11)
get_data(result,parrten11,text11,r"用\W来匹配特殊字符")
