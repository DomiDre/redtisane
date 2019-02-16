from setuptools import setup, find_packages


with open('README.md') as f:
  readme = f.read()

with open('LICENSE') as f:
  license = f.read()

setup(
  name='redtisane',
  version='0.0.1',
  description='Reduction Script for TISANE data of NIST',
  url='https://github.com/DomiDre/redtisane',
  author='Dominique Dresen',
  author_email='dominique.dresen@uni-koeln.de',
  license=license,
  long_description=readme,
  install_requires=[],
  python_requires='>2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
  platforms=['Linux'],
  package_dir={'redtisane': 'redtisane'},
  packages=find_packages(
    exclude=(
      '_build',
      'docs',
      '_static',
      '_templates'
      'tests',
      'examples'
      )
  ),
  keywords='tisane nist sans reduction'
)
