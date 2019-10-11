try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My project',
	'author': 'My Name',
	'url': 'URL to get it at.',
	'download url': 'Where to download it.',
	'author email': 'My email.',
	'version': '0,1',
	'install requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
	}

setup(**config)

