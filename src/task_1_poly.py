"""
出题者：柳文章，安徽大学人工智能学院
出题日期：2025.11.8

任务：编写函数 `poly_eval(coeffs: list, x: float) -> float`

- 对输入的多项式进行求解。
- 多项式的参数存于形参 `coeffs` 中，其类型为列表。
- 自变量的取值为形参 `x`，其类型为浮点型。
- 最终结果计算精度为保留小数点后四位（提示：使用 round() 函数确定输出结果精度）。
"""


def poly_eval(coeffs: list, x: float) -> float:
    """
    计算给定多项式在指定 x 值处的结果。

    多项式的形式为：
        a0 + a1*x + a2*x^2 + ... + an*x^n
    其中系数列表 coeffs = [a0, a1, a2, ..., an]。

    Args:
        coeffs (list): 多项式的系数列表，从常数项到最高次项。
        x (float): 要代入的自变量值。

    Returns:
        float: 多项式在给定 x 处的值。

    Example:
        >>> poly_eval([2, -3, 1], 5)
        12.0
        # 因为计算结果为 2 - 3*5 + 1*(5^2) = 12
    """
    # TODO: 在下方完成程序


if __name__ == "__main__":
    coef = [0.1, 0.2]
    x = 3.0
    y = poly_eval(coeffs=coef, x=x)
    print(f"The Result of the polynomial is {y}.")
