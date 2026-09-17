# 创建：
# company_info = ("贵州三人行", "财税服务", 2026)
# 完成：
# 输出公司名称
# 输出业务类型
# 输出年份
# 然后故意尝试修改：
# company_info[2] = 2027
# 观察报错。
# 最后把这一行注释掉，让程序恢复正常运行。
company_info = ("贵州三人行","财税服务",2026)
company_name, business_type, year = company_info
print("公司名称：", company_name)
print("业务类型：", business_type)
print("年份：", year)
# company_info[2] = 2027
# Traceback (most recent call last):
#   File "F:\Day90_py\Day5\tuple_test_2.py", line 16, in <module>
#     company_info[2] = 2027
#     ~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment