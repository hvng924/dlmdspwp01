from typing import List
import numpy as np
import pandas as pd

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

def list_to_dataframe(lst: List[dict]) -> pd.DataFrame:
    columns = {}

    for item in lst:
        for column in item.keys():
            if column not in columns:
                columns[column] = []
            columns[column].append(item[column])

    return pd.DataFrame(data=columns)