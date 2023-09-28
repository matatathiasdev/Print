from pyautogui import press
from importlib import util
import importlib

if util.find_spec("pandas") is not None:
    print("ok")