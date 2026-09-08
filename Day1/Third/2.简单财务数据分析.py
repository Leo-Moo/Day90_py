# 输入某公司的：
#
# 期初余额
# 本期增加
# 本期减少
#
# 计算：
#
# 期末余额 = 期初余额 + 本期增加 - 本期减少
#
# 然后输出：
#
# ===== 账户余额 =====
#
# 期初余额：xxxx
# 本期增加：xxxx
# 本期减少：xxxx
# 期末余额：xxxx

qcye = float(input("请输入期初余额："))
Ben_in = float(input("请输入本期增加："))
Ben_out = float(input("请输入本期减少："))
qwye = qcye + Ben_in -Ben_out
print("====账户余额====")
print("期初余额：",qcye)
print("本期增加：",Ben_in)
print("本期减少：",Ben_out)
print("期末余额：",qwye)
