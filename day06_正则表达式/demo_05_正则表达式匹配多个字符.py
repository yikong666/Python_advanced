r"""
需求：查看正则表达式匹配多个字符的每一个形式
包括：* + ？ {m} {m,n}
使用正则匹配表达式去匹配
查看结果


步骤：
1.导包
2.编写正则匹配和表达式
3.打印结果并观察总结
"""

# 1.导包
import re

#打印的方法
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


# 匹配字符*
parrten1, text1 = r".*", "bz666_黑马"
result = re.match(pattern=parrten1, string=text1)
get_data(result,parrten1,text1,"用'.'来匹配任意字符串（除了换行符）")


parrten2, text2 = r".*", "\n\n\n12345"
result = re.match(pattern=parrten2, string=text2)
get_data(result,parrten2,text2,"用'.'来匹配任意字符串（除了换行符）")
# #匹配+
#
# parrten3, text3 = r".+", "bz666_黑马"
# result = re.match(pattern=parrten3, string=text3)
# get_data(result,parrten3,text3,"用'+'来匹配任意字符串（除了换行符）")
#
# parrten4, text4 = r".+", ""
# result = re.match(pattern=parrten4, string=text4)
# get_data(result,parrten4,text4,"用'+'来匹配任意字符串（除了换行符）")
#
# parrten5, text5 = r".?", "bz666_黑马"
# result = re.match(pattern=parrten5, string=text5)
# get_data(result,parrten5,text5,"用'？'来匹配任意字符串（除了换行符）")
#
# parrten6, text6 = r".?", ""
# result = re.match(pattern=parrten6, string=text6)
# get_data(result,parrten6,text6,"用'？'来匹配任意字符串（除了换行符）")
#
# parrten_bad1, text_bad1 = r"\d{6}", "1234567899999"
# result = re.match(pattern=parrten_bad1, string=text_bad1)
# get_data(result,parrten_bad1,text_bad1,"用{m}来匹配任意字符串（除了换行符）")
#
# parrten_good1, text_good1 = r"^\d{6}$", "123456"
# result = re.match(pattern=parrten_good1, string=text_good1)
# get_data(result,parrten_good1,text_good1,"用{m}来匹配任意字符串（除了换行符）")
#
#
# parrten_bad2, text_bad2 = r"\d{3,9}", "12890123124124124"
# result = re.match(pattern=parrten_bad2, string=text_bad2)
# get_data(result,parrten_bad2,text_bad2,"用{m}来匹配任意字符串（除了换行符）")
#
# parrten_good2, text_good2 = r"^\d{3,9}$", "1289011112"
# result = re.match(pattern=parrten_good2, string=text_good2)
# get_data(result,parrten_good2,text_good2,"用{m}来匹配任意字符串（除了换行符）")
#
