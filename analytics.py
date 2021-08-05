from typing import List


import numpy as np

def sum_deviations_squared(a: List[float], b: List[float]) -> float:
    """Calculate sum of deviations squared

    Args:
        a (List[float]): Value list A
        b (List[float]): Value list B

    Returns:
        float: sum of deviations squared
    """
    a = np.array(a)
    b = np.array(b)
    return np.sum((a - b) ** 2)