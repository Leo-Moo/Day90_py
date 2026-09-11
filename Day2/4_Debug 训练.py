balance = 0
# balance = 1000  正常余额
# balance = -1000 异常余额

# if balance = 0:
#   File "F:\Day90_py\Day2\4_Debug 训练.py", line 5
#     if balance = 0:
#        ^^^^^^^^^^^
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
# '='是赋值语句，‘==’才是等于

if balance > 0:
    print("正常余额")
elif balance < 0:
    print("异常余额")
else:
    print("已结清")