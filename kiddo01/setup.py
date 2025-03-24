from setuptools import setup, find_packages

setup(
    name='kiddo01',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'torch', 'transformers', 'accelerate', 'sentencepiece'
    ],
    entry_points={
        'console_scripts': [
            'kiddo01 = kiddo01.cli:main',
        ],
    },
    author='Kris Ledel',
    description='An AI-powered programming language with Mistral-7B integration',
    url='https://github.com/k05730/kiddo01',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
