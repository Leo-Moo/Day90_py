# 用户先输入：
#  今天一共有多少笔收入？
# 例如输入：
# 6
#  程序就循环 6 次，让用户输入每笔金额。
# 同时统计：
# 总收入
# 大额收入笔数
# 普通收入笔数
# 业务规则：
# 单笔金额 >= 10000
# → 大额收入
#  单笔金额 < 10000
# → 普通收入
#  这道题需要把 Day 2 和 Day 3 连起来：
#  for
# ↓
# input
# ↓
# float
# ↓
# 累计金额
# ↓
# if
# ↓
# 累计数量
#  不要直接搜索完整代码。
#  你应该先设计这些变量：
#  总收入需要一个什么初始值？
# 需要初始值为0
#  大额收入笔数初始是多少？
# 0
#  普通收入笔数初始是多少？
# 0
total_income = 0
max_income, min_income = 0, 0
today_income = int(input("今天有多少笔收入？\n"))
for i in range(today_income):
    signle_income = float(input(f"请输入{i+1}笔收入："))
    total_income += signle_income
    if signle_income >= 10000:
        max_income += 1
    elif signle_income < 10000:
        min_income += 1
print(f"总收入：{total_income:.2f}")
print(f"大额收入笔数：{max_income}")
print(f"小额收入笔数：{min_income}")