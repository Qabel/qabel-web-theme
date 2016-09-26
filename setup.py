from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).parent

# Get the long description from the README file
with (here / 'README.rst').open() as f:
    long_description = f.read()

setup(
    name='qabel-web-theme',

    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    description='Theme for Qabel microservices',
    long_description=long_description,

    url='https://github.com/Qabel/qabel-web-theme',
    author='Qabel GmbH',

    license='QaPL',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages('src'),
    package_dir={'': 'src'},

    package_data={
        'qabel_web_theme': [
            'templates/*.html',
            'locale/*/LC_MESSAGES/*',
            'static/favicon.ico',
            'static/css/*.css',
            'static/img/*.png',
            'static/js/*.js',
            'static/fonts/*',
            'static/fonts/ssp/*',
        ],
    },
)
