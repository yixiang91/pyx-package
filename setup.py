import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="pyx-package",
    version="0.0.1",
    author="yixiang91",
    author_email="tayyixiang.91@gmail.com",
    description="An example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yixiang91/pyx-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires=">=3.6",
)
