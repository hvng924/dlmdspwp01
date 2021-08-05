from typing import List


import numpy as np

def sum_deviations_squared(a: List[float], b: List[float]):
    a = np.array(a)
    b = np.array(b)
    return np.sum((a - b) ** 2)