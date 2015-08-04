import click
import requests
from phue import Bridge, PhueRegistrationException


def discover():
    r = requests.get('https://www.meethue.com/api/nupnp')
    if r.status_code != 200:
        message = "No Bridge detected using: https://www.meethue.com/api/nupnp"
        raise click.ClickException(message)
    data = r.json().pop()
    return data['internalipaddress']


def connect(ip_address):
    try:
        return Bridge(ip_address)
    except PhueRegistrationException:
        message = 'Unable to connect to Bridge. Press the button on Bridge and try again'
        raise click.ClickException(message)
