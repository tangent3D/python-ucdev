from setuptools import setup, find_packages

setup(
      name='ucdev',
      version='0.0.1',
      packages=find_packages(),
      install_requires=[
            "cffi",
      ],
      entry_points={
            "console_scripts": ["gpio3=gpio3.cmd:main"],
    },
)
