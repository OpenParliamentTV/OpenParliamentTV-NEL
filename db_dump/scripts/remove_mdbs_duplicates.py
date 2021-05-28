import json
import ast

INFILE = './db_dump/data/mdbs/mdbs-formatted.json'
OUTFILE = './db_dump/data/mdbs/mdbs-formatted-nodups.json'

def remove_dups_from_list(list):
    if all(type(el) is dict for el in list):
        #we can't apply the set function to objects, lets convert them to string first
        strings = [str for str in set([str(el) for el in list])]
        return [ast.literal_eval(str) for str in strings]
    elif any(type(el) is dict for el in list):
        raise Exception("Can't remove list of duplicates. List of elements contains mixed types.")
    else:
        return [el for el in set(list)]

def get_all_keys(list_of_objects):
    keys = []
    for obj in list_of_objects:
        keys.extend(obj.keys())
    return set(keys)

def merge_dicts_additively(dicts):
    result = {}
    for key in get_all_keys(dicts):
        result[key] = []
        for dic in dicts:
            try:
                result[key].append(dic[key])
            except: #...exception: Key is not present
                pass
        result[key] =  remove_dups_from_list(result[key])
        #Remove lists with only 1 element
        if(len(result[key])==1):
            result[key] = result[key][0]
    return result


def group_records_by_ids(data):
    groups = []
    for id in set([d['id'] for d in data]):
        entries = [d for d in data if d['id'] == id]
        groups.append(entries)
    return groups

with open(INFILE) as infile:
    data = json.load(infile)
    cleaned = []
    groups = group_records_by_ids(data)
    for g in groups:
        merged = merge_dicts_additively(g)
        cleaned.append(merged)
    with open(OUTFILE, 'w') as outfile:
        json.dump(cleaned, outfile)


