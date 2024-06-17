import os, sys
import importlib.util
import shutil
import logging
from dataclasses import dataclass
import os
import subprocess

cdir = os.path.dirname(os.path.realpath(__file__))
path = cdir

cur_dir = os.getcwd()
parent_dir = os.path.realpath(os.path.join(os.path.dirname(cur_dir)))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
    sys.path.append(cur_dir)
sys.path.insert(1, ".")

from config.setting import ConfigStaticFiles

from gradio_client import Client, handle_file

client = Client(ConfigStaticFiles.huggingFace_rule
		api_name="/predict"
)
                
print(result)
