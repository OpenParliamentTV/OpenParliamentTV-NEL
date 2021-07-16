import requests

ENDPOINT_URL = "https://www.abgeordnetenwatch.de/api/v2/"

def get_faction(abgeordnetenwatchID, parliament_name="Bundestag"):
    response = requests.get(ENDPOINT_URL + "candidacies-mandates?politician[entity.politician.id]=" + str(abgeordnetenwatchID))
    print(response)
    mandates = response.json()['data']
    #only get candidacies that have a faction, only get factions relevant to the parliament
    mandates = [m for m in mandates if m.get('fraction_membership', None) is not None and parliament_name in m['fraction_membership'][0]['fraction']['label']]
    if(len(mandates)==0):
        return None
    faction_membership = mandates[0].get('fraction_membership')
    if isinstance(faction_membership, list) and len(faction_membership)>0:
        faction_membership = faction_membership[0]
    return faction_membership

def get_party(abgeordnetenwatchID):
    response = requests.get(ENDPOINT_URL + "politicians/" + str(abgeordnetenwatchID))
    print(response)
    politician_data = response.json()['data']
    party = politician_data.get('party')
    return party