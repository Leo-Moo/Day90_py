import pytest
from financial_risk import evaluate


@pytest.mark.parametrize(
    "income, expense, account_balance, expected_profit, expected_status",
    [
        (10000, 8000, 5000, 2000, "正常"),
        (8000, 10000, 5000, -2000, "需要关注"),
        (8000, 10000, -500, -2000, "高风险"),
        (10000, 8000, -500, 2000, "正常"),  # 当前代码结果；规则未定义
    ],
)
def test_evaluate(income, expense, account_balance, expected_profit, expected_status):
    profit, status = evaluate(income, expense, account_balance)

    assert profit == expected_profit
    assert status == expected_status