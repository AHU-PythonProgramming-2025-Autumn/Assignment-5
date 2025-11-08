from src.task_1_poly import poly_eval


def test_1_poly():
    coef = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    x = -3.0
    y = poly_eval(coeffs=coef, x=x)
    assert y == -1353.2


def test_1_poly_2():
    coef = [0.6, 0.7, 0.8]
    x = 3.0
    y = poly_eval(coeffs=coef, x=x)
    assert y == 9.9


def test_1_poly_3():
    coef = [0.1, 0.3, 0.4, 0.01] * 4
    x = -2.0
    y = poly_eval(coeffs=coef, x=x)
    assert y == 4456.38
