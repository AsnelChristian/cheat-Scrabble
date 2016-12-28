try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'cheat-Scrabble',
    'description': 'This is a very simple program to cheat scrabble',
    'author': 'Christian Asnel Ngoulla Sob',
    'download_url': 'https://github.com/Asnelchristian/cheat-Scrabble',
    'author_email': 'ngoullasob@gmail.com',
    'version': '0.1',
    'scripts': ['cheat_scrabble']
}

setup(**config)
