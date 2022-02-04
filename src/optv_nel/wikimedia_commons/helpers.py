import json, requests, re

def extract_image_license(image_name):

    commons_url_regex = r"(commons\.wikimedia\.org/wiki/File:|upload\.wikimedia\.org/wikipedia/commons/thumb/[^/]+/[^/]+/)([^/]+)"

    matches = re.findall(commons_url_regex, str(image_name))

    #print(len(matches[0]))

    if len(matches) > 0:
        image_name = matches[0][1]

    start_of_end_point_str = 'https://commons.wikimedia.org' \
                         '/w/api.php?action=query&titles=File:'
    end_of_end_point_str = '&prop=imageinfo&iiprop=extmetadata' \
                       '&iiextmetadatafilter=LicenseShortName|UsageTerms|AttributionRequired' \
                       '|Restrictions|Artist|ImageDescription|DateTimeOriginal&format=json'
    result = requests.get(start_of_end_point_str + image_name+end_of_end_point_str)
    result = result.json()
    page_id = next(iter(result['query']['pages']))
    image_info = result['query']['pages'][page_id]['imageinfo'][0]['extmetadata']

    attribution = {
        "creator": "Wikimedia Commons",
        "license": "CC-BY-SA"
    }

    try:
        dataCreator = image_info['Artist']['value']
        if dataCreator and dataCreator != "":
            attribution['creator'] = dataCreator.replace('\r', '').replace('\n', '')
    except KeyError:
        pass

    try:
        dataLicense = image_info['LicenseShortName']['value']
        if dataLicense and dataLicense != "":
            attribution['license'] = dataLicense
    except KeyError:
        pass

    vcard_creator_regex = r"id=\"creator\">(<bdi>.+</bdi>)"
    vcard_matches = re.findall(vcard_creator_regex, str(attribution['creator']))

    if len(vcard_matches) > 0:
        attribution['creator'] = vcard_matches[0]

    attribution['creator'] = remove_html_tags(attribution['creator']);
    
    return attribution

def remove_html_tags(text):
    import re
    clean = re.compile(r'<(?!\/?a).*?>')
    return re.sub(clean, '', text)

#attribution = extract_image_license('Marcel_Emmerich_November_2014.jpg')
#attribution = extract_image_license('https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/DIE_LINKE_Bundesparteitag_Mai_2014_Modrow,_Hans.jpg/300px-DIE_LINKE_Bundesparteitag_Mai_2014_Modrow,_Hans.jpg')
#print(attribution);