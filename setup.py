from setuptools import setup, find_packages

setup(
    name="gpt-json-sanitizer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    author="Muhammad Ali",
    author_email="muhammad.edtech@gmail.com",
    description="A package to fix JSON responses from ChatGPT",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/m-ali-awan/gpt-json-sanitizer.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
