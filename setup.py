from setuptools import setup

setup(
     name='zipfLaw',
     version='0.1.0',
     author='forthstate',
     packages=['zipfLaw'],
     install_requires=[
        'matplotlib',
        'pandas',
        'scipy',
        'pyyaml',
        'pytest'],
     entry_points={
        'console_scripts': [
            'countwords = zipfLaw.countwords:main',
            'collate = zipfLaw.collate:main',
            'plotcounts = zipfLaw.plotcounts:main']})
