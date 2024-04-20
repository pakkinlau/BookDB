from setuptools import setup, find_packages

setup(
    name='BookDB',
    version='0.1.1',
    description='A tool for populating book data into databases for big data processing',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Pak Kin Lau',
    author_email='pakkinlau.general@gmail.com',
    url='https://github.com/pakkinlau/BookDB',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        # Add dependencies here, e.g., 'requests', 'pandas', etc.
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)