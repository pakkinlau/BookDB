from setuptools import setup, find_packages

setup(
    name='BookDB',
    version='0.1.1',
    description='A tool for populating book data into databases for big data processing',
    long_description=open('README.md').read(),
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
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)