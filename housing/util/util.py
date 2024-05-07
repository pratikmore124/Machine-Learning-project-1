import yaml
from housing.exception import HousingException
import os,sys

#Util.py file is a helper function. It is not a part of the pipeline, but it help other functionality to work proprly.

# read yaml file
def read_yaml_file(file_path : str)->dict:
    try:
        with open(config_file_path,"rb") as yaml_file:
            config_info = yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e
