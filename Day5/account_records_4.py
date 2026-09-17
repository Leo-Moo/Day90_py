# 用户首先输入：
# 需要检查多少个科目？
# 假设：
# 3
# 然后逐个输入：
# 银行存款
# 15000
# 应收账款
# -2300
# 库存现金
# 0
# 每输入一个科目，你需要构造一个字典。
# 最终得到的逻辑结构应该类似：
# accounts
# 第1条
# ├── name
# ├── balance
# └── status
# 第2条
# ├── name
# ├── balance
# └── status
# 第3条
# ├── name
# ├── balance
# └── status
# 也就是说：
# 一个字典
# → 一条科目记录
# 一个列表
# → 保存很多条科目记录
# 最后统一遍历 accounts，输出：
# ========== 科目检查结果 ==========
# 1. 银行存款 | 15000.00 | 正常
# 2. 应收账款 | -2300.00 | 异常
# 3. 库存现金 | 0.00 | 已结清
# 今天暂时不要求统计异常占比。
# 先把数据结构真正搞懂。

subject_list = []

while True:
    try:
        subject = int(input("Please enter the subject number: "))
        break
    except ValueError:
        print("请输入数字！")


for i in range(subject):
    subject_name = input("Please enter the subject name: ")
    subject_name = subject_name.strip()
    ending_balance_num = float(input("Please enter the ending balance: : "))
    status= " "
    if ending_balance_num  > 0 :
        status = "正常"
    elif ending_balance_num  == 0 :
        status = "已结清"
    elif ending_balance_num  < 0 :
        status = "异常"
    accounts = {
            "科目名称": subject_name,
            "期末余额": ending_balance_num,
            "状态": status
        }
    subject_list.append(accounts)
for idx, accounts in enumerate(subject_list, start=1):
    print(f"{idx}. {accounts["科目名称"]} | {accounts["期末余额"]:.2f} | {accounts["状态"]}")

# account = {
#     "name": "银行存款",
#     "balance": 15000
# }
# # print(account[0])
# print(account["name"])
# print(account["balance"])