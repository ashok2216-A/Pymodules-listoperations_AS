from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Listoperations_AS_v0.0.1',
  version='0.0.1',
  description='A very basic List Operations',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Ashok kumar',
  author_email='ashoksiva2216@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['listoperators', 'sumlist', 'countlist', 'swaplist', 'averageoflist'],
  packages=find_packages(),
  install_requires=[''] 
)
