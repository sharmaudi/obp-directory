import os
import yaml


def resolve_data(file_name):
    r = os.path.dirname(os.path.abspath(__file__))
    return f"{r}/../data/{file_name}"


def resolve_config(file_name):
    r = os.path.dirname(os.path.abspath(__file__))
    return f"{r}/../config/{file_name}"


def load_jwk_config():
    dir_config = {}
    try:
        config_location = resolve_data('config.yaml')
        with open(resolve_data('config.yaml'), 'r') as f:
            dir_config = yaml.load(f)
    except Exception as ex:
        print(ex)
        print(f"Error while loading config.yaml. Make sure that config.yaml is mounted at location {config_location}")
    return dir_config
