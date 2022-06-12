import setuptools

setuptools.setup(
    name='pipsinfo',
    version='0.0.3',
    scripts=['pipsinfo'],
    author="saba",
    author_email="sabaathelet@gmail.com",
    description="python pip package infromation",
    long_description="will list the pip package which are installed in the system",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operation System :: OS Independent",
    ],
)

