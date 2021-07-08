import json
import ast

INFILE = './db_dump/data/mdbs/mdbs-formatted.json'
OUTFILE = './db_dump/data/mdbs/mdbs-final.json'

def remove_dups_from_list(thelist):
    print("List", thelist)
    if all(type(el) is dict for el in thelist):
        #we can't apply the set function to objects, lets convert them to string first
        strings = [str for str in set([str(el) for el in thelist])]
        return [ast.literal_eval(str) for str in strings]
    elif all(isinstance(el, list) for el in thelist):
        #we can't apply the set function to lists, lets convert them to string first
        strings = [str for str in set([str(el) for el in thelist])]
        return [ast.literal_eval(str) for str in strings]
    else:
        return [el for el in set(thelist)]

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
        #Remove value None only if there are other values present
        if(len(result[key])>1):
            try: 
                result[key].remove(None) 
            except:
                pass
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

def get_id(mdb):
    key = int(mdb['id'][1:]) #remove the Q from the ID
    return key

with open(INFILE) as infile:
    data = json.load(infile)
    cleaned = []
    groups = group_records_by_ids(data)
    for g in groups:
        print(g)
        merged = merge_dicts_additively(g)
        cleaned.append(merged)
    cleaned.sort(key=get_id, reverse=True)
    with open(OUTFILE, 'w', encoding='utf8') as outfile:
        json.dump(cleaned, outfile, ensure_ascii=False)


