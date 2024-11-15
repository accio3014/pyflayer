from setuptools import setup, find_packages

setup(
    name='pyflayer',
    version='0.0.0',
    description='API Python Library for Learning Python Basics using Minecraft and Mineflayer.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='accio3014',
    author_email='accio3014@gmail.com',
    url='https://github.com/accio3014/pyflayer',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        # 'required-package>=1.0.0',
    ],
    license='MIT',
    keywords='minecraft python mineflayer education',
)
