import os
from typing import Any, Dict

import function

CMD_TO_FUNC = {
    'filter': function.filter_query,
    'map':function.map_query ,
    'unique':function.unique_query ,
    'sort': function.sort_query,
    'limit': function.limit_query,
    'regex' : function.regular_func,
}

VALID_CMD_PARAMS =(
    'filter',
    'map',
    'unique',
    'sort',
    'limit',
    'regex',
 )

def get_file(name)->str:
    file = os.path.join(DATA_DIR,str(name))
    return file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE = os.path.join(DATA_DIR,"apache_logs.txt")

def build_query(name:str,cmd:str,param:str,data:dict)->dict:
    if data is None:
        with open(get_file(name)) as f:
            prepared_data = list(map(lambda x:x.strip(), f))
    else:
        prepared_data = data

    return CMD_TO_FUNC[cmd](param = param, data = prepared_data) # type: ignore


