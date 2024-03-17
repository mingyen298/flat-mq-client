from setuptools import setup,find_packages

setup(
    name='flat-mq-client',
    version='0.0.1',
    description='',
    author='Charlie Hsieh',
    author_email='oe327188@gmail.com',
    python_requires=">=3.9",
    url='https://github.com/mingyen298/flat-mq-client',
    packages=find_packages(exclude=["tests*"]), 
    install_requires=[
        "gmqtt==0.6.14"
    ],  
)
