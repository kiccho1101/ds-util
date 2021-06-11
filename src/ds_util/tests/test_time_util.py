import time
from unittest.mock import patch

from ds_util.time_util import TimeUtil


@TimeUtil.timer_wrapper
def _func():
    time.sleep(0.1)


@patch("builtins.print")
def test_timer(mock_print):
    with TimeUtil.timer("test task"):
        time.sleep(0.1)
    printed: str = mock_print.call_args_list[1].args[0]
    assert printed.startswith("[test task] done")


@patch("builtins.print")
def test_timer_wrapper(mock_print):
    _func()
    printed: str = mock_print.call_args_list[1].args[0]
    assert printed.startswith("[_func] done")
