import glob
from os.path import basename, dirname, isfile

from config import *
from ling import *
from ling.helpers import *
from ling.helpers.SQL import *
from ling.resources import *
from ling.utils import *


def __list_all_modules():
    mod_paths = glob.glob(f"{dirname(__file__)}/*.py")

    return [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
