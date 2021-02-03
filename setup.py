from setuptools import find_packages, setup

setup(
    name="aiobtcrpc",
    packages=find_packages(),
    version="0.1.1",
    description="Asynchronous Bitcoin RPC Client",
    author="@biobdeveloper",
    url="https://github.com/biobdeveloper/aiobtcrpc",
    license="MIT",
    install_requires=["aiohttp==3.7.3"],
    test_suite="tests",
    setup_requires=["pytest-runner"],
    python_requires=">=3.8"
)
