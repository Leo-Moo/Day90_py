# 输入：
#
# 公司名称
# 本月收入
# 本月支出
# 账户余额
#
# 先计算：
#
# 利润 = 收入 - 支出
#
# 然后根据以下规则判断：
#
# 利润 < 0 且 账户余额 < 0
# → 高风险
#
# 利润 < 0 但 账户余额 >= 0
# → 需要关注
#
# 利润 >= 0 且 账户余额 >= 0
# → 正常
#
# 这里你需要第一次真正使用：
#
# and
#
# 不要查完整答案。
#
# 先自己把需求翻译成三个问题：
#
# 第一种情况需要同时满足什么？
#
# 第二种情况需要同时满足什么？
#
# 第三种情况需要同时满足什么？
# and就是需要两个条件同时满足，不满足就不执行
# 然后再决定 if / elif / else 怎么排列。
from Day1.Second.day01 import company, exxpense

company_name = input("Please input your company name: ")
income = input("Please input your income: ")
expense = input("Please input your expense: ")
account_balance = input("Please input your account balance: ")

profit = income - expense

if profit < 0 and account_balance < 0:
    status = "高风险"
elif profit < 0 and account_balance >= 0:
    status = "需要关注"
else:
    status = "正常"
