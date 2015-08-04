from setuptools import setup


setup(
    name='HUE',
    version='1.0',
    py_modules=['huecli'],
    install_requires=[
        'Click==4.1',
        'phue==0.8',
        'requests==2.7.0',
        'PyYAML==3.11'
    ],
    entry_points='''
        [console_scripts]
        huecli=huecli:cli
    ''',
)
