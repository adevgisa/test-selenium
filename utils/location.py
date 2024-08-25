import pycountry
import gettext
import requests

russian = gettext.translation('iso3166-2', pycountry.LOCALES_DIR,
                              languages=['ru'])
russian.install()

_ = russian.gettext

def get_ip():
    response = requests.get('https://api.ipify.org?format=json').json()

    return response["ip"]

def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

    return response

def get_region_name_by_ip():
    location = get_location()
    subdiv = pycountry.subdivisions.get(code=location['country_code'] + '-' + location['region_code'])

    return _(subdiv.name)
