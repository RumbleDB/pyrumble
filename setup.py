import setuptools

setuptools.setup(
    # Name of the module
    name='rumbledb',
    version='1.17.0',
    # Details
    description='IPython wrapper to use the Rumble framework.',
    # The project's main homepage.
    url='https://github.com/RumbleDB/rumble',
    # Author details
    author='Ghislain Fourny',
    author_email='gfourny@inf.ethz.ch',
    # License
    license='Apache License 2.0',
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    keywords='rumble jsoniq IPython jupyter',
    classifiers=[
        # Intended Audience.
        'Intended Audience :: Developers',
        # Operating Systems.
        'Operating System :: OS Independent',
    ],
    install_requires=['requests', 'jupyter'],
)
