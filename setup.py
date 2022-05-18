import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="file-transfer-tools",
    author="wyg1997",
    author_email="wangyinggang@foxmail.com",
    description="Transfer files simply in shell",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wyg1997/transfer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["transfer=transfer.command_line:main"],
    },
)
