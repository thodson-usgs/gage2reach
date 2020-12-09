from setuptools import setup

setup(name='gage2reach',
      version='0.1',
      description='Lookup NHDplus reach ID for USGS streamgage.',
      url='https://github.com/thodson-usgs/gage2reach',
      author='Timothy Hodson',
      author_email='thodson@usgs.gov',
      license='CC0',
      packages=['gage2reach'],
      install_requires=[
      ],
      include_package_data=True,
      package_data={'gage2reach': ['*.bz2']},
      zip_safe=False)
