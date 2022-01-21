def check_for_dups(list):
    ids = [el['id'] for el in list]
    dups = set([id for id in ids if ids.count(id) > 1])
    print("There are",len(dups), "Duplicates: ", dups)

def group_socials(obj):
    twitter = obj.pop('twitter', None)
    facebook = obj.pop('facebook', None)
    instagram = obj.pop('instagram', None)
    group = []
    if twitter is not None:
        group.append({'label': 'Twitter', 'id': twitter})
    if facebook is not None:
        group.append({'label': 'Facebook', 'id': facebook})
    if instagram is not None:
        group.append({'label': 'Instagram', 'id': instagram})
    return group

def group_additional_information(obj):
    abgeordnetenwatchID = obj.pop('abgeordnetenwatchID', None)
    group = {}
    if abgeordnetenwatchID is not None:
        group['abgeordnetenwatchID'] = abgeordnetenwatchID
    return group