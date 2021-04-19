import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="rsaf",
    version='0.1',
    author="Ian Nesbitt",
    author_email="ian.nesbitt@gmail.com",
    license='GPLv3',
    description="conversion of archived miniSEED data to Raspberry Shake UDP-formatted ASCII, and forwarding of that data via UDP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raspishake/rsaf",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['obspy', 'rsudp'],
    entry_points = {
        'console_scripts': [
            'rsaf=rsaf.run:main',
            'packetize=rsaf.packetize:main',
            ],
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Development Status :: 4 - Beta",
    ],
)
