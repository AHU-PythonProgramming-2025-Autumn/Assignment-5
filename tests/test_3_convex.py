from src.task_3_convex import convex_hull


def test_convex_hull_1():
    points = [(0.5, 0.1), (1.1, 0.9), (0.1, 0.7), (-0.9, -0.8), (0.7, -2.0)]
    support_points = convex_hull(points)
    expected_points = [(-0.9, -0.8), (0.7, -2.0), (1.1, 0.9), (0.1, 0.7)]
    assert support_points == expected_points


def test_convex_hull_2():
    points = [(1.3, 0.8), (-0.6, -1.1), (-0.6, 1.1), (0.2, -0.5), (-0.2, -0.1),
              (-1.0, 0.3), (0.4, 0.2), (-0.3, 1.2), (0.9, -1.3), (-0.2, -0.5)]
    support_points = convex_hull(points)
    expected_points = [(-1.0, 0.3), (-0.6, -1.1), (0.9, -1.3), (1.3, 0.8), (-0.3, 1.2), (-0.6, 1.1)]
    assert support_points == expected_points
