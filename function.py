from typing import Optional
import re

def filter_query(param: str,data)->list:
    return list(filter(lambda x: param in x, data))

def map_query(param:str,data:str)->list:
    col_number = int(param)
    return list(map(lambda  x: x.split(' ')[col_number],data))

def unique_query(data:str,*args,**kwargs)->list:
    return list(set(data))

def sort_query(param:str,data)->list:
    reverse = False if param == 'asc'else True
    return sorted(data, reverse = reverse)

def limit_query(param:str,data)->list:
    limit: int = int(param)
    return list(data)[:limit]

def regular_func(param:str,data:str)->str:
    return re.search(param:str,data:str)
