# 做一个财务科目名称清洗器。用户输入类似：
#
#    银行存款
#
# 程序输出清理后的名称和字符长度。然后自己尝试处理：
#
# 应收账款-客户A
#
# 把它拆成：
# 科目：应收账款
# 客户：客户A
subject_name = input("Please input your subject name:")
subject_name = subject_name.strip()
print(f"程序处理之后的名称为：{subject_name},字符长度为：{len(subject_name)}")

if "-" in subject_name:
    parts = subject_name.split("-", 1) # split只切1次，防止名字里面还有横杠
    subject = parts[0]
    customer = parts[1]
    print(f"科目：{subject}")
    print(f"客户：{customer}")
else:
    print(f"科目：{subject_name}")
    print("客户：无")

print(type(subject_name))