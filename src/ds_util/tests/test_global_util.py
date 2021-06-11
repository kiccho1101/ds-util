import os
import time

from ds_util.global_util import GlobalUtil


def test_os():
    assert "PYTHONHASHSEED" not in os.environ
    GlobalUtil.seed_everything(111)
    assert os.environ["PYTHONHASHSEED"] == "111"


def test_get_metric():
    t0 = time.time()
    t, m, per = GlobalUtil.get_metric()
    print("t", t)
    print("m", m)
    print("per", per)
    assert isinstance(t, float)
    assert isinstance(m, float)
    assert isinstance(per, float)
    assert t > t0
    assert 0 <= per <= 100
