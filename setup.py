import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask_mysqlcp",
    version="1.1.0",
    author="AlaBouali",
    author_email="trap.leader.123@gmail.com",
    description="Flask extension to create connection pools with pymysql2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlaBouali/flask_mysqlcp",
    python_requires=">=2.7",
    install_requires=['pymysql2'],
    packages=["flask_mysqlcp"],
    license="MIT License",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License ",
    ],
)
