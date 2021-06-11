import pickle
from pathlib import Path
from typing import Any, Union

import numpy as np
import pandas as pd

from ds_util.time_util import TimeUtil


class FileUtil:
    @staticmethod
    def load_csv(filepath: Union[str, Path], verbose: bool = True, **kwargs):
        if verbose:
            with TimeUtil.timer(f"Read {str(filepath)}"):
                return pd.read_csv(filepath, **kwargs)
        return pd.read_csv(filepath, **kwargs)

    @staticmethod
    def save_npy(arr: np.ndarray, filepath: Union[str, Path], verbose: bool = True):
        with open(filepath, "wb") as f:
            if verbose:
                with TimeUtil.timer(f"Save {str(filepath)}"):
                    np.save(f, arr)
            else:
                np.save(f, arr)

    @staticmethod
    def load_npy(filepath: Union[str, Path], verbose: bool = True) -> np.ndarray:
        with open(filepath, "rb") as f:
            if verbose:
                with TimeUtil.timer(f"Load {str(filepath)}"):
                    arr = np.load(f)
            else:
                arr = np.load(f)
        return arr

    @staticmethod
    def save_pickle(obj: Any, filepath: Union[str, Path], verbose: bool = True):
        with open(filepath, "wb") as f:
            if verbose:
                with TimeUtil.timer(f"Save {str(filepath)}"):
                    pickle.dump(obj, f)
            else:
                pickle.dump(obj, f)

    @staticmethod
    def load_pickle(filepath: Union[str, Path], verbose: bool = True) -> Any:
        with open(filepath, "rb") as f:
            if verbose:
                with TimeUtil.timer(f"Load {str(filepath)}"):
                    obj = pickle.load(f)
            else:
                obj = pickle.load(f)
        return obj
