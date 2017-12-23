import requests

PAYLOAD={'Accept':'application/json', 'apikey': ''}
BASE_URL = 'https://search.onboard-apis.com'

def get_community_info(area_id):
    r = requests.get(BASE_URL+'/communityapi/v2.0.0/Area/Full/', headers=PAYLOAD, params={'AreaId': area_id})
    return r.content

if __name__ == "__main__":
   print(get_community_info("CO44003"))
