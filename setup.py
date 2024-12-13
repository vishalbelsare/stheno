from setuptools import find_packages, setup

requirements = [
    "numpy>=1.16",
    "fdm>=0.5.0",
    "algebra>=1",
    "plum-dispatch>=2",
    "backends>=1.4.11",
    "backends-matrix>=1.2.11",
    "mlkernels>=0.3.6",
    "wbml>=0.4.0",
]

setup(
    packages=find_packages(exclude=["docs"]),
    python_requires=">=3.6",
    install_requires=requirements,
    include_package_data=True,
)
