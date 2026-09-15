# 要求：
# 先输入：今天有多少笔收入？
# 例如：4
# 然后输入：
# 1200
# 8500
# 15000
# 3200
# 把所有收入保存到：income_list
# 最终先打印：[1200.0, 8500.0, 15000.0, 3200.0]
# 然后再遍历：
# income_list
# 计算：
# 总收入
# 大额收入笔数
# 普通收入笔数
# 规则还是：
# >= 10000 → 大额
# < 10000 → 普通
# 注意：
# 今天我要求你：
# 先保存，再统计。
# 不要在输入的时候直接全部统计完。
# 原因是我要让你理解：
# 录入数据
# ↓
# 保存原始数据
# ↓
# 统一处理
# 这更接近以后真正的数据处理流程。
today_income = int(input("今天有多少笔收入？\n"))
income_list = []
max_income,normal_income , total_income= 0, 0, 0
for i in range(today_income):
    income = float(input(f"请输入第{i+1}笔收入："))
    income_list.append(income)
    if income >= 10000:
        max_income += 1
    elif income < 10000:
        normal_income += 1
    total_income += income
print(f"今天总共有{today_income}笔收入")
print(f"大额收入笔数为：{max_income}")
print(f"小额收入笔数为：{normal_income}")
print(f"总收入为：{total_income}")

