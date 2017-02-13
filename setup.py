from setuptools import setup

setup(name='PythonPackaging',
      version='0.1',
      description='Sample Python package',
      url='https://github.com/smruthiEJ/PythonPackaging',
      author='Smruthi Elapavuluri',
      author_email='jsmruthi@gmail.com',
      license='OpenSource',
      packages=['date'],
      scripts=['hello.py'], zip_safe=True)
      #zip_safe= True --> will not unzip the egg file once installed. 
