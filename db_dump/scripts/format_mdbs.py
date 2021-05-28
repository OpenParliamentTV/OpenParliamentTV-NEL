import json

DICT = {
    'mdbLabel': 'xxxlabel'
}

def rename(prop):
    try:
        return DICT[prop]
    except:
        return prop

def group_socials(obj):
    twitter = obj.pop('twitter', None)
    facebook = obj.pop('facebook', None)
    instagram = obj.pop('instagram', None)
    group = {}
    if twitter is not None:
        group['twitter'] = twitter
    if facebook is not None:
        group['facebook'] = facebook
    if instagram is not None:
        group['instagram'] = instagram
    return group

def group_additionalInformation(obj):
    abgeordnetenwatchID = obj.pop('abgeordnetenwatchID', None)
    group = {}
    if abgeordnetenwatchID is not None:
        group['abgeordnetenwatchID'] = abgeordnetenwatchID
    return group

def reformat(obj):
    flat = {key : value['value'] for (key, value) in obj.items()}
    id = flat.pop('mdb').split('/')[-1]
    label = flat.pop('mdbLabel')
    birthDate = flat.pop('dateOfBirth', None)
    new = {
        'type': 'memberOfParliament', 
        'id': id, 
        'label': label, 
        'birthDate': birthDate,
        'socialMediaURIs': group_socials(flat),
        'additionalInformation': group_additionalInformation(flat),
        **flat
    }
    print(new)
    return new
    #return 


INFILE = 'db_dump/data/mdbs/mdbs.json'
OUTFILE = 'db_dump/data/mdbs/mdbs-formatted.json'

# map over the entries and reformat each of them (reformatting means changing property names or grouping properties)
with open(INFILE) as infile:
    data = json.load(infile)
    entries = [reformat(entry) for entry in data['results']['bindings']]
    for e in entries:
        print(json.dumps(e, indent=4, sort_keys=True))
    with open(OUTFILE, 'w') as outfile:
        json.dump(entries, outfile)

# Save the file
