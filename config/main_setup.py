"""
This file directs the model to:
    - location of modflow run files
    - create folders for output runs
    ...#TODO
"""
import sys
import os

import config.run_setup as rs

# path to package modules
#sys.path.append('../utils')
#sys.path.append('../preprocessing')

# name of config file
config = 'config.yaml'

# location of exec files
exe_name = os.path.abspath(os.path.join("bin", "mf6.exe"))


# run setup --------------

# open config file
ws_data = rs.open_yaml(config)

# make output dir for run
run_dir = rs.mk_run_dir(ws_data)
data_dir = ws_data['workspace']['data_dir']