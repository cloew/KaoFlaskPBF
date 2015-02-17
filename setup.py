from distutils.core import setup

setup(name='pbf_kao_flask',
      version='.1',
      description="Programmer's Best Friend Utility Extension for pbf_kao_flask",
      author='', # Add your name here
      author_email='', # Add your e-mail here
      packages=['pbf_kao_flask', 'pbf_kao_flask.Commands', 'pbf_kao_flask.templates'],
      #package_data = {'pbf_kao_flask.templates':[]}, # Add template files
     )