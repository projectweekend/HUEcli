import os
import yaml
import click


CONFIG_FILE_PATH = os.path.join(os.path.expanduser('~'), '.huecli/config')


def create(ip_address):
    data = {'ip_address': str(ip_address)}
    if not os.path.exists(os.path.dirname(CONFIG_FILE_PATH)):
        os.makedirs(os.path.dirname(CONFIG_FILE_PATH))
    with open(CONFIG_FILE_PATH, 'w+') as f:
        f.write(yaml.dump(data, default_flow_style=False))
    return data


def get():
    try:
        with open(CONFIG_FILE_PATH, 'r') as f:
            data = f.read()
    except IOError:
        raise click.ClickException("No config found. Use 'setup' command")
    return yaml.load(data)
