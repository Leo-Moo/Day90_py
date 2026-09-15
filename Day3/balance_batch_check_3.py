# 用户首先输入：  需要检查多少个科目？
# 然后逐个输入：
# 科目名称、 期末余额
# 例如：
# 银行存款
# 15000
# 应收账款
# -2300
# 库存现金
# 0
# 沿用 Day 2 的规则：
# 余额 > 0
# → 正常余额
# 余额 == 0
# → 已结清
# 余额 < 0
# → 异常余额
# 但是这次还要在所有科目处理结束后输出汇总：
# ========== 检查结果 ==========
# 检查科目数：3
# 正常：1
# 已结清：1
# 异常：1
# 异常科目占比：33.33%
# 注意：
# 异常占比 = 异常数量 / 总数量 × 100
# 你需要自己考虑一个边界：
# 如果用户输入检查科目数量为 0，计算异常占比会发生什么？
# 先运行、观察，再决定怎么用 Day 2 的 if 解决。
# 这就是今天的 Debug/边界测试任务。
total_sum, normal_balance,unusual_balance , over_balance = 0, 0, 0, 0
subject = int(input("要检查几个科目？\n"))
for i in range(subject):
    subject_name = input("科目名称：")
    ending_balance = float(input("期末余额："))
    if ending_balance > 0 :
        normal_balance += 1
    elif ending_balance < 0 :
        unusual_balance += 1
    elif ending_balance == 0 :
        over_balance += 1

total_sum = normal_balance + unusual_balance + over_balance

if total_sum > 0:
    Abnormal_balance_proportion = unusual_balance / total_sum * 100
else:
    Abnormal_balance_proportion = 0

print("检查结果")
print(f"检查科目数：{subject}")
print(f"正常：{normal_balance}")
print(f"已结清：{over_balance}")
print(f"异常：{unusual_balance}")
print(f"异常科目占比：{Abnormal_balance_proportion:.2f}%")

# count = 1
#curl.exe -I https://github.com
# while count <= 5:
#     print(count)

count = 1

while count <= 5:
    print(count)
    count = count + 1
