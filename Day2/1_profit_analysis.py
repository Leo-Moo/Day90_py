# 需求：
#
# 用户输入：
#
# 公司名称
# 本月收入
# 本月支出
#
# 计算：
#
# 利润 = 收入 - 支出
#
# 然后程序自动判断：
#
# 利润 > 0
# → 盈利
#
# 利润 == 0
# → 收支持平
#
# 利润 < 0
# → 亏损
#
# 输出可以类似：
#
# ===== 月度经营分析 =====
# 公司：贵州XX有限公司
# 收入：50000.00 元
# 支出：42000.00 元
# 利润：8000.00 元
# 经营状态：盈利
#
# 我不给完整代码。
#
# 今天变量命名开始正式要求：
#
# company_name
# income
# expense
# profit
company_name = input("Please enter Company Name: ")
income = float(input("Please enter Income: "))
expense = float(input("Please enter Expense: "))

profit = income - expense

print("The company name is",company_name)
print("The income is",income)
print("The expense is",expense)
print("The profit is",profit)

if profit > 0:
    status = "盈利"
elif profit == 0:
    status = "收支平衡"
else:
    status = "亏损"

print(f"经营状态：{status}")


