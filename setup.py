
from setuptools import setup, find_packages


def description():
    return """
    py-http-facade is a simple HTTP Façade for easy request making
    """

setup(
    name="py_http_facade",
    version="0.1",
    author="rtesini",
    author_email="rtesini@gmail.com",
    description=description(),
    license="MIT",
    keywords="python http request api rest facade",
    url="http://github.com/rtesini/py-http-facade",
    packages=find_packages(exclude=['tests']),
    install_requires=[''],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ]
)
