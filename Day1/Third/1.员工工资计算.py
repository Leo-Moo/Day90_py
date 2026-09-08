# 输入：
# 员工姓名
# 基本工资
# 奖金
# 扣款
#
# 计算：
# 实发工资 = 基本工资 + 奖金 - 扣款
#
# 最后输出类似：
# 员工：张三
# 基本工资：5000 元
# 奖金：800 元
# 扣款：200 元
# 实发工资：5600 元
Ygname = input("请输入员工姓名：")
Bsgongzi = float(input("请输入基本工资："))
Bonus = float(input("请输入奖金："))
KouKuan = float(input("请输入扣款："))
Shi_Gongzi = Bsgongzi + Bonus - KouKuan
print("员工：",Ygname)
print("基本工资：",Bsgongzi,"元")
print("奖金：",Bonus,"元")
print("扣款：",KouKuan,"元")
print("实发工资：",Shi_Gongzi,"元")
