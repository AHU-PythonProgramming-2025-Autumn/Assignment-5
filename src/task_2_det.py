"""
出题者：柳文章，安徽大学人工智能学院
出题日期：2025.11.8

任务：编写函数 `determinant(matrix: list) -> float`

- 对输入的方阵求解行列式的值。
- 输入矩阵为形参 `matrix`，其类型为列表，列表中存放的是子列表，子列表中存放的是浮点型数据。
- 最终结果计算精度为保留小数点后四位（提示：使用 round() 函数确定输出结果精度）。
"""


def determinant(matrix: list) -> float:
    """
    计算输入方阵的行列式（Determinant）值。

    使用递归展开（Laplace Expansion）计算行列式。
    若矩阵为 1×1 或 2×2，则直接返回结果；否则按第一行进行展开。
    注意：如果输入不是方阵（行数与列数不同），则输出字符串“行列数需保持相同。”

    Args:
        matrix (list): 一个二维方阵（列表嵌套列表），
            例如 [[1, 2], [3, 4]] 或 [[2, -1, 0], [1, 3, 4], [0, 2, 5]]。

    Returns:
        float: 输入矩阵的行列式值。

    Example:
        >>> determinant([[1, 2], [3, 4]])
        -2.0

        >>> determinant([[2, -1, 0], [1, 3, 4], [0, 2, 5]])
        19.0
    """
    # TODO: 在下方完成程序


if __name__ == "__main__":
    m = [[2, -1, 0], [1, 3, 4], [0, 2, 5]]
    det = determinant(m)
    print(f"The determinant of the matrix is {det:.4f}.")
