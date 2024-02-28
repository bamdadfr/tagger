from setuptools import find_packages, setup

setup(
    name="tagger",
    version="0.0.0",
    description="tagger",
    author="Bamdad Sabbagh",
    author_email="hi@bamdad.fr",
    packages=find_packages(),
    install_requires=[
        # List any dependencies your module has here
    ],
    entry_points={
        "console_scripts": ["tag = tagger.main:main"],
    },
)
