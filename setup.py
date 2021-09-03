from setuptools import setup, find_packages

setup(
    name="lusyringe",
    version="1.0.0",
    description="LuSyringe is a documentation injection tool for your classes when using Fast API",
    url="https://gitlab.luizalabs.com/enzo.ferreira/lusyringe",
    author="Enzo Ferrari",
    license='MIT',
    packages=find_packages(include=["lusyringe", "lusyringe.*"]),
    install_requires=[
        'pydantic>=1.8.2'
    ]
)
