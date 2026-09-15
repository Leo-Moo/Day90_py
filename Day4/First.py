accounts = []
for i in range(3):
    account = input("请输入科目名称：")
    accounts.append(account)
for j in range(3):
    print(f"第{j+1}个科目是：{accounts[j]}")
