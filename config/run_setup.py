import yaml
import os
from datetime import datetime

def open_yaml(config):
    try:
        with open(config, 'r') as f:
            data = yaml.safe_load(f)
            return data
    except yaml.YAMLError as exc:
        print(exc)

def mk_run_dir(ws_data):

    # Location to save all the model run files
    output_dir = ws_data['workspace']['output_dir']
    sim_name = ws_data['workspace']['sim_name']

    run_dir = run_dir_name(sim_name, output_dir)

    # Setup working directories
    work_directories = (
        os.path.join(output_dir, f"{run_dir}"),
        os.path.join(output_dir, f"{run_dir}/figures")
    )

    for work_dir in work_directories:
        if not os.path.isdir(work_dir):
            os.makedirs(work_dir)
    
    return work_directories[0]

def run_dir_name(sim_name, output_dir):
    """
    name directory:
    {date_today}_run{count}_{sim_name}
    """
    
    # todays date
    today = datetime.today().strftime('%Y%m%d')
    # count of num files in dir
    run_num = len(os.listdir(output_dir)) + 1

    if sim_name is None:
        return f'{today}_run{run_num}'
    else:
        return f'{today}_run{run_num}_{sim_name}'

