from ds_util.string_util import StringUtil


def test_camel_to_snake():
    assert StringUtil.camel_to_snake("TestString") == "test_string"
    assert StringUtil.camel_to_snake("teststring") == "teststring"
    assert StringUtil.camel_to_snake("test_string") == "test_string"
    assert StringUtil.camel_to_snake("__test_string") == "__test_string"
    assert StringUtil.camel_to_snake("ABCString") == "a_b_c_string"
    assert StringUtil.camel_to_snake("_ABCString") == "__a_b_c_string"


def test_rename_col_for_lightgbm():
    assert StringUtil.rename_col_for_lightgbm("test_string") == "test_string"
    assert StringUtil.rename_col_for_lightgbm("test string") == "test_string"
    assert StringUtil.rename_col_for_lightgbm("test~string") == "test_string"
    assert StringUtil.rename_col_for_lightgbm("test|string") == "test_string"
    assert StringUtil.rename_col_for_lightgbm("test|~string") == "test__string"
