# 假设你在工作中需要人工录入一条客户收款数据。
# 程序要求用户输入：
#
# 客户名称
# 期初余额
# 本期收入
# 本期支出
# 然后自行计算：
# 期末余额 = 期初余额 + 本期收入 - 本期支出
# 最终输出类似：
#
# ========== 客户资金摘要 ==========
#
# 客户名称：贵州XX有限公司
# 期初余额：10000.00 元
# 本期收入：8500.00 元
# 本期支出：3200.00 元
# 期末余额：15300.00 元
# KfName = input("请输入公司名称：")
# qcye = float(input("请输入期初余额："))
# BQSR = float(input("请输入本期收入："))
# BQZC = float(input("请输入本期支出："))
# QWYE = qcye + BQSR - BQZC
# print("="*5,"客户资金摘要","="*5)
# print("客户名称：",KfName)
# print("期初余额：",qcye)
# print("本期收入：",BQSR)
# print("本期支出：",BQZC)
# print("期末余额：",QWYE)


# KmName = input("请输入科目名称：")
# qcye = float(input("请输入期初余额："))
# BQJF = float(input("请输入本期借方："))
# BQDF = float(input("请输入本期贷方："))
# QWYE = qcye + BQJF - BQDF
#
# print(f"科目名称：{KmName:}")
# print(f"期初余额：{qcye:.2f}")
# print(f"本期借方：{BQJF:.2f}")
# print(f"本期贷方：{BQDF:.2f}")
# print(f"期末余额：{QWYE:.2f}")

opening_balance = input("请输入期初余额：")
income = input("请输入本期收入：")

ending_balance = opening_balance + income

print(ending_balance)
# 为什么没有报错？
# 因为两个都是字符串类型，所以就拼接在一起了
# 为什么结果不是 15000？
# 因为不是整型或者浮点型
# 应该修改哪两个地方？
# 加入一个转换

# Day 1
#
# 1. input() 得到的数据默认是什么类型？
# str
# 2. int() 和 float() 分别适合什么数据？
# 个数、有小数的
# 3. "10000" + "5000" 为什么得到 "100005000"？
# 因为是字符串类型
# 4. 今天哪个地方我还需要看示例才能写出来？
# 无