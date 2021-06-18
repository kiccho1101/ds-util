import ds_util


def test_version():
    assert ds_util.__version__ is not None
    assert isinstance(ds_util.__version__, str)
