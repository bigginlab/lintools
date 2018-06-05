
from setuptools import setup

setup(name='lintools',
      version='06.2018',
      description='Illustrates protein-ligand interactions',
      url='https://github.com/bigginlab/lintools.git',
      author='Phil Biggin and Laura Domicevica',
      author_email='philip.biggin@bioch.ox.ac.uk',
      license='GPL',
      packages=['lintools','lintools.analysis'],
      entry_points={
          'console_scripts': [
              'lintools = lintools.__main__:main'
          ]
      },
      zip_safe=False)
