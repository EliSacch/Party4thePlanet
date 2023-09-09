import os
import requests
from urllib.parse import urlencode

# Start code from CodingEntepreneurs
# https://www.youtube.com/watch?v=ckPEY2KppHc
def extract_coordinates(address):
    # Get url from address
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": os.environ.get('MAPS_API_KEY')}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    # Get coordinates from url
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return ()
    latlng = {}
    try:
        latlng = r.json()['results'][0]['geometry']['location']
    except:  # noqa
        pass
    return latlng.get("lat"), latlng.get("lng")
# end of code from CodingEntepreneurs