import os
import function

CMD_TO_FUNC = {
    'filter': function.filter_query,
    'map':function.map_query ,
    'unique':function.unique_query ,
    'sort': function.sort_query,
    'limit': function.limit_query,
}

VALID_CMD_PARAMS =(
    'filter',
    'map',
    'unique',
    'sort',
    'limit',
 )

def get_file(name):
    file = os.path.join(DATA_DIR,str(name))
    return file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE = os.path.join(DATA_DIR,"apache_logs.txt")

def build_query(cmd,param,data):
    if data is None:
        with open(FILE) as f:
            prepared_data = list(map(lambda x:x.strip(), f))
    else:
        prepared_data = data

    return CMD_TO_FUNC[cmd](param = param, data = prepared_data)


