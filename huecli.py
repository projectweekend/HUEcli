import click
from hue import bridge, configuration


def get_bridge():
    config = configuration.get()
    return bridge.connect(config['ip_address'])


@click.group()
def cli():
    """
    Control Philips HUE lighting from the command line
    """


@cli.command()
def setup():
    """
    Setup connection to Bridge
    """
    ip_address = bridge.discover()
    bridge.connect(ip_address)
    config = configuration.create(ip_address)

    message = 'Config created for IP address: {0}'.format(config['ip_address'])
    click.echo(message)


@cli.command()
def status():
    """
    List status of available lights
    """
    b = get_bridge()
    for light in b.lights:
        message = '{0}: {1}'.format(light.name, 'ON' if light.on else 'OFF')
        click.echo(message)


@cli.command()
@click.argument('action')
def lights(action):
    """
    Control all lights
    """
    b = get_bridge()
    for light in b.lights:
        if action == 'on':
            light.on = True
        elif action == 'off':
            light.on = False


@cli.command()
@click.argument('name_of_light')
@click.argument('action')
def light(name_of_light, action):
    """
    Control a single light
    """
    name_of_light = name_of_light.encode('utf-8')
    b = get_bridge()
    if action == 'on':
        b.set_light(name_of_light, 'on', True)
    if action == 'off':
        b.set_light(name_of_light, 'on', False)
