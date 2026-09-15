# 用户输入：
# 需要录入多少个科目？
# 假设 3。
# 然后故意输入：
#    银行存款
# 应收账款
#   库存现金
# 每输入一个后：
# 用 strip() 清理。
# 保存到列表。
# 最终输出：
# ========== 科目清单 ==========
# 1. 银行存款
# 2. 应收账款
# 3. 库存现金
# 共 3 个科目
# 今天你可以继续使用：
# for i in range(...)
# 也可以尝试：
# for account in accounts:
# 如果编号不会处理，不要查完整答案，先自己想。
subject_num = int(input("需要录入多少个科目？\n"))
subject_list = []
for i in range(subject_num):
    subject_name = input("请输入科目名称：")
    subject_name = subject_name.strip()
    subject_list.append(subject_name)
print("========== 科目清单 ==========")
# enumerate
for idx, name in enumerate(subject_list, start=1):
    print(f"{idx}. {name}")
print(f"共{len(subject_list)}个科目")

