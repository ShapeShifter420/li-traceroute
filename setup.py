from setuptools import setup, find_packages

setup(name='li-traceroute',

      version='1.0',

      url='https://github.com/ShapeShifter420/li-traceroute',

      description='python simple traceroute ICMP/UDP+ICMP for linux',

      packages=find_packages(exclude=['tests']),

      long_description=open('README.md').read(),

      test_suite='test',

      install_requires=['matplotlib']
)