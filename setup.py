from setuptools import setup, find_packages

setup(
    name = 'recast-api-demos',
    description = 'API demos for API SDK',
    author = 'Christian Bora',
    author_email = 'borachristian@gmail.com',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'recast-api'
        ],
    dependency_links = [
        'https://github.com/cbora/recast-api/tarball/master#egg=recast-api-0.0.1',
        ]
    )
