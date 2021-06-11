from abc import ABCMeta, abstractmethod
from pathlib import Path
from typing import List, Optional

import pandas as pd

from ds_util.string_util import StringUtil
from ds_util.test_util import TestUtil
from ds_util.time_util import TimeUtil


class BaseFeature(metaclass=ABCMeta):
    def __init__(
        self,
        path: Path,
        name: Optional[str] = None,
        data_type: str = "feather",
        merge_type: str = "concat",
        on: List[str] = [],
        how: str = "left",
        required_cols: List[str] = [],
    ):
        ALLOWED_DATA_TYPES = ["feather", "pickle"]
        ALLOWED_MERGE_TYPES = ["concat", "merge"]

        self.path = path
        if name is None:
            self.name = StringUtil.camel_to_snake(self.__class__.__name__)
        else:
            self.name = name
        self.data_type = data_type
        self.merge_type = merge_type
        self.on = on
        self.how = how
        self.required_cols = required_cols
        if data_type not in ALLOWED_DATA_TYPES:
            raise ValueError("data_type must be in {}".format(ALLOWED_DATA_TYPES))
        if merge_type not in ALLOWED_MERGE_TYPES:
            raise ValueError("merge_ must be in {}".format(ALLOWED_DATA_TYPES))

    def save(self, fe_df: pd.DataFrame):
        filepath = self.path / f"{self.name}.{self.data_type}"
        if self.data_type == "pickle":
            fe_df.to_pickle(str(filepath))
        else:
            fe_df.to_feather(str(filepath))

    def read(self) -> pd.DataFrame:
        filepath = self.path / f"{self.name}.{self.data_type}"
        if self.data_type == "pickle":
            fe_df = pd.read_pickle(str(filepath))
        else:
            fe_df = pd.read_feather(str(filepath))
        return fe_df

    def merge(self, df: pd.DataFrame, fe_df: pd.DataFrame) -> pd.DataFrame:
        if self.merge_type == "merge":
            drop_cols = [col for col in fe_df.columns if col not in self.on]
            df = df.drop(drop_cols, axis=1, errors="ignore")
            df = df.merge(fe_df, on=self.on, how=self.how)
        else:
            df.loc[:, fe_df.columns.tolist()] = fe_df.values
        return df

    @abstractmethod
    def create_feature(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        raise NotImplementedError

    def main(self, df: pd.DataFrame, rerun: bool = False, **kwargs):
        for required_col in self.required_cols:
            if required_col not in df.columns:
                raise ValueError(f"{required_col} not in df")

        filepath = self.path / f"{self.name}.{self.data_type}"
        if rerun or not filepath.exists():
            with TimeUtil.timer(f"create_feature: {self.name}"):
                fe_df = self.create_feature(df, **kwargs)
                self.save(fe_df)
        else:
            with TimeUtil.timer(f"read_feature: {self.name}"):
                fe_df = self.read()
        TestUtil.assert_any(len(fe_df), len(df))
        df = self.merge(df, fe_df)
        return df
