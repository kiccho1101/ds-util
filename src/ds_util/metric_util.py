from dataclasses import dataclass
from typing import List, Union

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

from ds_util.test_util import TestUtil


@dataclass
class ClassificationMetric:
    acc: float
    precision: float
    recall: float
    f1: float


class MetricUtil:
    @staticmethod
    def get_classification_metric(
        y_true: Union[List[int], np.ndarray, pd.Series],
        y_pred: Union[List[int], np.ndarray, pd.Series],
    ) -> ClassificationMetric:
        if isinstance(y_true, pd.Series):
            y_true = y_true.tolist()
        if isinstance(y_pred, pd.Series):
            y_pred = y_pred.tolist()

        if isinstance(y_true, np.ndarray):
            y_true = y_true.tolist()
        if isinstance(y_pred, np.ndarray):
            y_pred = y_pred.tolist()

        TestUtil.assert_any(len(y_true), len(y_pred))
        for i in range(len(y_true)):
            assert (
                isinstance(y_true[i], int) or y_true[i].is_integer()
            ), f"{y_true[i]}(y_true[{i}]) is not integer"
            assert (
                isinstance(y_pred[i], int) or y_pred[i].is_integer()
            ), f"{y_pred[i]}(y_true[{i}]) is not integer"

        return ClassificationMetric(
            acc=accuracy_score(y_true, y_pred),
            precision=precision_score(y_true, y_pred),
            recall=recall_score(y_true, y_pred),
            f1=f1_score(y_true, y_pred),
        )
