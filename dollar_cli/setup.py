from setuptools import setup, find_packages

# This file helps Python understand how to install your project
setup(
    name='dollar-cli',          # The name of your package
    version='0.1.0',            # Version number
    packages=find_packages(),   # Automatically find all your Python packages
    include_package_data=True,  # Include any other files needed
    
    # These are the external libraries your project needs
    install_requires=[
        'Click',        # For building the command-line interface
        'SQLAlchemy',   # For working with the database
    ],
    
    # This creates the 'dollar' command that users can run
    entry_points='''
        [console_scripts]
        dollar=dollar_cli.cli:cli
    ''',
)