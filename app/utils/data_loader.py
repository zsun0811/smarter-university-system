
import os
import json

def load_data(file_name:str) -> any:
    """
    Loads data from the data directory.
    """
    fpath = os.path.join('data',file_name)
    if not os.path.exists(fpath):
        return []
    with open(fpath, 'r') as fin:
        return json.load(fin)
    
def save_data(file_name:str, data:any) -> None:
    """
    Saves updated data back to the data directory.
    """
    fpath = os.path.join('data',file_name)
    with open(fpath, 'w+') as fout:
        json.dump(data, fout, indent=2, sort_keys=True)