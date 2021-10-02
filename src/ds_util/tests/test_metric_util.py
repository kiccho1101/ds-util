import numpy as np
import pandas as pd
from ds_util.metric_util import MetricUtil


def test_classification_metric_list():
    y_true = [0, 0, 1, 1]
    y_pred = [0, 0, 1, 1]
    metric = MetricUtil.get_classification_metric(y_true, y_pred)
    assert metric.acc == 1
    assert metric.precision == 1
    assert metric.recall == 1
    assert metric.f1 == 1


def test_classification_metric_np():
    y_true = np.array([0, 0, 1, 1])
    y_pred = np.array([0, 0, 1, 1])
    metric = MetricUtil.get_classification_metric(y_true, y_pred)
    assert metric.acc == 1
    assert metric.precision == 1
    assert metric.recall == 1
    assert metric.f1 == 1


def test_classification_metric_pd():
    y_true = pd.Series([0, 0, 1, 1])
    y_pred = pd.Series([0, 0, 1, 1])
    metric = MetricUtil.get_classification_metric(y_true, y_pred)
    assert metric.acc == 1
    assert metric.precision == 1
    assert metric.recall == 1
    assert metric.f1 == 1


def test_regression_metric_list():
    y_true = [0, 0, 1, 1]
    y_pred = [0, 0, 1, 1]
    metric = MetricUtil.get_regression_metric(y_true, y_pred)
    assert metric.mae == 0
    assert metric.mse == 0
    assert metric.rmse == 0


def test_regression_metric_np():
    y_true = np.array([0, 0, 1, 1])
    y_pred = np.array([0, 0, 1, 1])
    metric = MetricUtil.get_regression_metric(y_true, y_pred)
    assert metric.mae == 0
    assert metric.mse == 0
    assert metric.rmse == 0


def test_regression_metric_pd():
    y_true = pd.Series([0, 0, 1, 1])
    y_pred = pd.Series([0, 0, 1, 1])
    metric = MetricUtil.get_regression_metric(y_true, y_pred)
    assert metric.mae == 0
    assert metric.mse == 0
    assert metric.rmse == 0
