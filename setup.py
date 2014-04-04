from setuptools import setup, find_packages
setup(
    name='edgegrid-python', 
    version='1.0', 
    description='{OPEN} client authentication protocol for python-requests',
    author='Jonathan Landis',
    author_email='jlandis@akamai.com',
    url='https://gsd.akamai.com/stash/users/jlandis/repos/edgegrid-python',
    packages=find_packages(),
    install_requires = [
        'requests'
    ],
    license='LICENSE.txt'
)