import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'README.md')) as f:
    README = f.read()


REQUIREMENTS = [
    'requests',
    'facebookads',
    'django==1.5'
]

setup(
    name='facebook_login',
    version='0.1',
    description='Django facebook server side login',
    author='rasca0027',
    author_email='rasca0027@gmail.com',
    long_description=README,
    scripts=[],
    url='https://github.com/rasca027/django-facebook-server-login',
    packages=find_packages(),
    license='Apache 2.0',
    platforms='Posix; MacOS X; Windows',
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet',
    ]
)
