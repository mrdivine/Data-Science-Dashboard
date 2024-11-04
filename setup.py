from setuptools import setup, find_packages

# Read dependencies from requirements.txt
def parse_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()

setup(
    name="profile-self-assessment-generator",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=parse_requirements("requirements.txt"),
)