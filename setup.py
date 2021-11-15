from setuptools import setup

setup(
     name='py_zipf',
     version='0.1',
     author='forthstate'
     packages=['py_zipf'],
     install_requires=[
          'matplotlib',
          'pandas',
          'scipy',
          'pyyaml',
          'pytest'],
      entry_points={
        'console_scripts': [
            'countwords = pyzipf.countwords:main',
            'collate = pyzipf.collate:main',
            'plotcounts = pyzipf.plotcounts:main']})
