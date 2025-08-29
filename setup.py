from setuptools import setup, find_packages

setup(
    name='dollar-cli',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'SQLAlchemy',
        'Alembic',
        'python-dateutil' 
    ],
    entry_points='''
        [console_scripts]
        dollar=dollar_cli.cli:cli
    ''',
)