# 需求：公司今天有 5 笔收入，让用户依次输入。
#
# 最终输出：
#
# 第1笔收入：...
# 第2笔收入：...
# ...
# 收入总额：xxxxx.xx 元
#
# 要求必须使用：
#
# for
# range()
# 累计变量
#
# 不要写 5 次 input()。
#
# 你需要自己解决一个小问题：
#
# 如何让提示文字自动显示“第 1 笔、第 2 笔……”？
#
# 提示只给到这里：
#
# for i in range(...):
#
# 想一下 i 能不能参与输出。
total_income = 0
for i in range(1,6):
    financial_risk = int(input("请输入收入："))
    print(f"第{i}笔收入：{financial_risk:.2f}")
    total_income += financial_risk
print(f"收入总额：{total_income:.2f}")
#But I don't understand why can't input continuously


