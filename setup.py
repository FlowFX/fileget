from setuptools import setup, find_packages

setup(
    name='fileget',
    version='0.1.0',
    license='GPL3',
    description='Download images from the internets',

    author='Florian Posdziech',
    author_email='fileget-718498@flowfx.de',
    url='https://flowfx.de',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['click', 'requests'],

    entry_points={
        'console_scripts': [
            'fileget = fileget.cli:cli',
        ]
    },
)
