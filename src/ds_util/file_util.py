import pickle
from pathlib import Path
from typing import Any, Union

import numpy as np
import pandas as pd

from ds_util.time_util import TimeUtil


class FileUtil:
    @staticmethod
    def load_csv(
        filepath: Union[str, Path], verbose: bool = True, logger=None, **kwargs
    ):
        if verbose:
            with TimeUtil.timer(f"Read {str(filepath)}", logger):
                return pd.read_csv(filepath, **kwargs)
        return pd.read_csv(filepath, **kwargs)

    @staticmethod
    def save_npy(
        arr: np.ndarray, filepath: Union[str, Path], verbose: bool = True, logger=None
    ):
        with open(filepath, "wb") as f:
            if verbose:
                with TimeUtil.timer(f"Save {str(filepath)}", logger):
                    np.save(f, arr)
            else:
                np.save(f, arr)

    @staticmethod
    def load_npy(
        filepath: Union[str, Path], verbose: bool = True, logger=None
    ) -> np.ndarray:
        with open(filepath, "rb") as f:
            if verbose:
                with TimeUtil.timer(f"Load {str(filepath)}", logger):
                    arr = np.load(f)
            else:
                arr = np.load(f)
        return arr

    @staticmethod
    def save_pickle(
        obj: Any, filepath: Union[str, Path], verbose: bool = True, logger=None
    ):
        with open(filepath, "wb") as f:
            if verbose:
                with TimeUtil.timer(f"Save {str(filepath)}", logger):
                    pickle.dump(obj, f)
            else:
                pickle.dump(obj, f)

    @staticmethod
    def load_pickle(
        filepath: Union[str, Path], verbose: bool = True, logger=None
    ) -> Any:
        with open(filepath, "rb") as f:
            if verbose:
                with TimeUtil.timer(f"Load {str(filepath)}", logger):
                    obj = pickle.load(f)
            else:
                obj = pickle.load(f)
        return obj
