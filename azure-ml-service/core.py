#!/usr/bin/python3

#%% Import dependencies
import os
import yaml


#%% Experiment functions 

def get_experiment_config(lab_name):
    with open('config.yml', 'r', encoding='utf-8') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    
    experiment_config = config['default'][lab_name]
    experiment_config['core'] = config['default']['core']
    
    return experiment_config


def init_experiment(config):
    os.makedirs(os.path.join(config['core']['expriments_root_dir'], config['working_subdir']), exist_ok=True)
    print('Experiment {} was initialized successfully.'.format(config['experiment_name']))
