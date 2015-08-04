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
