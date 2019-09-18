from setuptools import setup, find_packages

setup(name='li-traceroute',

      version='1.5',

      url='https://github.com/ShapeShifter420/li-traceroute',

      description='python simple traceroute ICMP/UDP+ICMP for linux',

      packages=['li_traceroute'],

      zip_safe=False,

      long_description=open('README.md').read(),

      test_suite='test',

      install_requires=['matplotlib'],

      entry_points={
        'console_scripts': ['li-trace = li_traceroute.traceroute:main']}
      )
