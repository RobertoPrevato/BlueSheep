from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='bluesheep',
      version='0.0.3',
      description='HTTP Server/Client microframework for Python asyncio',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
          'Operating System :: OS Independent',
          'Framework :: AsyncIO'
      ],
      url='https://github.com/RobertoPrevato/BlueSheep',
      author='Roberto Prevato',
      author_email='roberto.prevato@gmail.com',
      keywords='BlueSheep web framework',
      platforms=['*nix'],
      license='MIT',
      packages=['bluesheep'],
      install_requires=[],
      include_package_data=True,
      zip_safe=False)
