from typing import Any, List, Optional

import pandas as pd


class EdaUtil:
    @staticmethod
    def get_cut_agg_df(
        df: pd.DataFrame,
        col: str,
        target: str,
        cut_method: str = "cut",
        n_cut: int = 10,
        agg: List[str] = ["count", "mean", "std"],
        max_value: Optional[Any] = None,
    ):
        cut_col = f"{col}_cut"
        df[cut_col] = df[col]
        if max_value is not None:
            df.loc[df[cut_col] > max_value, cut_col] = max_value
        if cut_method == "qcut":
            df[cut_col] = pd.qcut(df[cut_col], n_cut)
        else:
            df[cut_col] = pd.cut(df[cut_col], n_cut)
        agg_df = df.groupby(cut_col)[target].agg(agg)
        return agg_df
