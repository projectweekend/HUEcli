import click
import requests
from phue import Bridge, PhueRegistrationException


NO_BRIDGE_DETECTED = "No Bridge detected using: https://www.meethue.com/api/nupnp."
NO_BRIDGE_CONNECTION = "Unable to connect to Bridge. Press the button on Bridge and try again."


def discover():
    r = requests.get('https://www.meethue.com/api/nupnp')
    if r.status_code != 200:
        raise click.ClickException(NO_BRIDGE_DETECTED)
    try:
        data = r.json().pop()
    except IndexError:
        raise click.ClickException(NO_BRIDGE_DETECTED)
    return data['internalipaddress']


def connect(ip_address):
    try:
        return Bridge(ip_address)
    except PhueRegistrationException:
        raise click.ClickException(NO_BRIDGE_CONNECTION)
