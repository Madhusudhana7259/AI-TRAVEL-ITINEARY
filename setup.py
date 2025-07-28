from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ai-travel-agent",
    version="0.1",
    author="Madhusudhana",
    packages=find_packages(),
    install_requires = requirements,
)