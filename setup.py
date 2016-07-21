from setuptools import setup

setup(
		name='twitterscraper',
		version='0.1.1',
		description='Tool for scraping Tweets',
		url='https://github.com/taspinar/twitterscraper',
		author='Ahmet Taspinar',
		author_email='taspinar@gmail.com',
		license='MIT',
		packages=['twitterscraper'],
		install_requires=[
          'bs4',
      ],
		zip_safe=False
		)
