from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    name='Python_Packaging',
    version='0.1.1',
    url='http://github.com/smruthiEJ/PythonPackaging',
    author='Smruthi Elapavuluri',
    author_email='jsmruthi@gmail.com',
    license='OpenSource',
    description='Cython based Python Packaging',
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("demo",["demo.py"],language='c++')])
