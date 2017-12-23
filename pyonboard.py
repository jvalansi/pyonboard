import requests
import json

BASE_URL = 'https://search.onboard-apis.com'

def get_community_info(apikey, accept, area_id):
    r = requests.get(BASE_URL+'/communityapi/v2.0.0/Area/Full/', headers={'apikey': apikey, 'accept': accept}, params={'AreaId': area_id})
    return json.loads(r.content)["response"]

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('apikey', 
                        help='The API key')
    parser.add_argument('--accept', choices=['application/json','application/xml'], default='application/json',
                        help='Data type for the response')
    parser.add_argument('--area_id', 
                        help='Requested area id : State (STxxx), County (COxxx), Zip Code (ZIxxx), Census Place (PLxxx), County Subdivision (CSxxx), Maponics Neighborhood (NDxxx), Maponics Residential, Subdivision (RSxxx), Maponics Metro (MTxxx)')

    args = parser.parse_args()
    print(json.dumps(get_community_info(args.apikey, args.accept, args.area_id), indent=4))
