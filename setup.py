from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="swapsub",
    version="2.0.2",
    author="cybytess",
    author_email="p2002817@outlook.com",
    description="a subtitle file format converter",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/cybytess/swapsub",

    packages=find_packages(),

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 ',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Video',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Operating System :: Unix'
    ]

)
