from setuptools import setup, find_packages

with open("README.md", "r") as fh:
      long_description = fh.read()

setup(
      name='airos_tasks',
      version='0.1',
      description='Ubiquti AirOS SSH helper',
      author='Denis Bezrodnykh',
      author_email='denis.bee@gmail.com',
      url='https://github.com/denisbee/airos-tasks',
      python_requires='>=3.5',
      packages=find_packages(),
      long_description=long_description,
      long_description_content_type="text/markdown",
      install_requires=[ 'paramiko~=2.7.1', 'cached_property~=1.5' ]
)