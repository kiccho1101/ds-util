import re


class StringUtil:
    @staticmethod
    def camel_to_snake(s: str):
        return re.sub(r"(?<!^)(?=[A-Z])", "_", s).lower()

    @staticmethod
    def rename_col_for_lightgbm(col: str):
        return "".join(c if c.isalnum() else "_" for c in str(col))
