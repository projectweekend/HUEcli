from setuptools import setup


setup(
    name='HUE',
    version='1.1',
    py_modules=['huecli'],
    install_requires=[
        'Click==6.2',
        'phue==0.8',
        'requests==2.7.0',
        'PyYAML==3.11'
    ],
    entry_points='''
        [console_scripts]
        hue=huecli:cli
    ''',
)
