import click
from hue import bridge, configuration


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
def list():
    """
    List available lights
    """
    config = configuration.get()
    b = bridge.connect(config['ip_address'])
    for light in b.lights:
        message = '{0}: {1}'.format(light.name, 'ON' if light.on else 'OFF')
        click.echo(message)


@cli.command()
@click.argument('name')
@click.argument('state')
def light(name, state):
    """
    Control a light
    """
    config = configuration.get()
    b = bridge.connect(config['ip_address'])
    name = name.encode('utf-8')
    if state == 'on':
        b.set_light(name, 'on', True)
    if state == 'off':
        b.set_light(name, 'on', False)
