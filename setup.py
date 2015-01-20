# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-genericimports',
    version='0.1.b3',
    author=u'Oscar Carballal Prego',
    author_email='oscar.carballal@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='http://github.com/clione/django-genericimports',
    license='BSD licence, see LICENCE file',
    description='Import any CSV or XLS file regardless of data types, headers or foreignkeys.',
    long_description=open('README').read(),
    zip_safe=False,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
