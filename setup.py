# setup.py
from setuptools import setup, find_packages

setup(
    name='robotframework-restbridge',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'robotframework',
    ],
    entry_points={
        'console_scripts': [
            # Add any command-line scripts here
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your module',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/your_module',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)