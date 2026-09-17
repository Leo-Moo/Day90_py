# 让用户输入：
# 科目名称：
# 期末余额：
# 例如：
# 银行存款
# 15000
# 然后自己根据余额判断：
# > 0  → 正常
# == 0 → 已结清
# < 0  → 异常
# 最后组织成：
# account = {
#     ...
# }
# 最终程序输出类似：
# ========== 科目信息 ==========
# 科目名称：银行存款
# 期末余额：15000.00
# 状态：正常
# 要求：
# 必须使用字典
# 必须通过 key 读取数据
# 不能只创建 name、balance、status 三个普通变量然后直接打印

accounts = {
    "科目名称" : " " ,
    "期末余额" : 0.0 ,
    "状态" : " "
}
subject_name = input("Please enter the subject name: ")
subject_name = subject_name.strip()
accounts["科目名称"] = subject_name
ending_balance_num = float(input("Please enter the ending balance: : "))
accounts["期末余额" ] = ending_balance_num
if accounts["期末余额"] > 0 :
    accounts["状态"] = "正常"
elif accounts["期末余额"] == 0 :
    accounts["状态"] = "已结清"
elif accounts["期末余额"] < 0 :
    accounts["状态"] = "异常"
print("="*9,"科目信息","="*9)
print(f"科目名称：{accounts["科目名称"]}")
print(f"期末余额：{accounts["期末余额"]}")
print(f"状态：{accounts["状态"]}")