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

#
# company_name = input("Please input your company name: ")
# income = float(input("Please input your income: "))
# expense = float(input("Please input your expense: "))
# account_balance = float(input("Please input your account balance: "))
#
# profit = income - expense
#
# if profit < 0 and account_balance < 0:
#     status = "高风险"
# elif profit < 0 and account_balance >= 0:
#     status = "需要关注"
# else:
#     status = "正常"
#
# print("company name:", company_name)
# print(f"income:{income:.2f}", income)
# print(f"expense:{expense:.2f}")
# print(f"profit:{profit:.2f}")
# print(f"balance:{account_balance:.2f}",)
# print(f"account balance:{ account_balance:.2f}")
# print(f"status:{status:.2f}")

# 第三件事，给程序补上最终输出，至少输出：
#
# 公司名称
# 收入
# 支出
# 利润
# 账户余额
# 风险状态
#
# 金额全部保留两位小数。
#
# 第四件事，至少测试下面 4 组数据：
#
# 收入 10000，支出 8000，余额 5000
# → 正常
#
# 收入 8000，支出 10000，余额 5000
# → 需要关注
#
# 收入 8000，支出 10000，余额 -500
# → 高风险
#
# 收入 10000，支出 8000，余额 -500
# → ?


def evaluate(income, expense, account_balance):

    profit = income - expense

    if profit < 0 and account_balance < 0:
        status = "高风险"
    elif profit < 0 and account_balance >= 0:
        status = "需要关注"
    else:
        status = "正常"

    return profit, status

if __name__ == "__main__":
    company_name = input("Please input your company name: ")
    income = float(input("Please input your income: "))
    expense = float(input("Please input your expense: "))
    account_balance = float(input("Please input your account balance: "))

    profit, status = evaluate(income, expense, account_balance)

    print(f"公司名称：{company_name}")
    print(f"收入：{income:.2f}")
    print(f"支出：{expense:.2f}")
    print(f"利润：{profit:.2f}")
    print(f"账户余额：{account_balance:.2f}")
    print(f"风险状态：{status}")