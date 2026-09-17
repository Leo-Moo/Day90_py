# 自己创建：
# accounts = ["银行存款", "库存现金", "应收账款"]
# 完成以下操作：
# 检查“银行存款”是否存在
# 检查“固定资产”是否存在
# 删除“库存现金”
# 输出删除后的列表
# 输出列表当前元素数量
#
# 要求使用今天学习的：
#
# in
# remove()
# len()
accounts = ["银行存款", "库存现金", "应收账款"]
subject_name = input("Please input your subject name:")
if subject_name.strip():
    accounts.append(subject_name)
else:
    print("输入为空，不予添加")
# accounts.append(subject_name)
find_subject_name = input("Please input you want to find the subject name:")
find_subject_name = find_subject_name.strip()
if find_subject_name in accounts:
    print(f"{find_subject_name}存在")
    while True:
        choice = input("Do you want to delete it? Y or N:")
        choice = choice.strip()
        choice = choice.upper()
        if choice == "Y":
            accounts.remove(find_subject_name)
            break
        elif choice == "N":
            print("取消删除")
            break
        else:
            print("输入错误，请重新输入！")
else:
    print(f"{find_subject_name}不存在，无法删除")
print(f"当前列表为：{accounts}")
print(f"当前列表元素数量为{len(accounts)}个")