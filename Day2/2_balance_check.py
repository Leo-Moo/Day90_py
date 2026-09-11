# 输入：
#
# 科目名称
# 期末余额
#
# 根据余额判断：
#
# 余额 > 0
# → 正常余额
#
# 余额 == 0
# → 已结清
#
# 余额 < 0
# → 异常余额，请核查
#
# 金额要求输出两位小数。
#
# 这道题的重点不是计算，而是把：
#
# 业务规则 → 条件表达式 → 程序输出
#
# 转换出来。
#
# 以后你处理几千行 Excel，本质也是：
#
# 读取某一行
# ↓
# 判断数据
# ↓
# 满足规则？
# ↓
# 打标签
#
# 今天只是先用一个变量练习。

subject_name = input("Please enter Subject_name:")
ending_balance = float(input("Please enter ending_balance "))

if ending_balance > 0:
    status = "正常余额"
elif ending_balance == 0:
    status = "已结清"
else:
    status = "异常余额，请复查！"

print(status)