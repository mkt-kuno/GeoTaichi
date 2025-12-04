#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Setup script for GeoTaichi package
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements from requirements.sh or define them here
requirements = [
    'taichi>=1.6.0',
    'numpy>=1.20.0',
    'scipy',
    'trimesh',
    'imageio',
    'matplotlib',
    'psutil',
    'pynvml>=11.4.1',
    'shapely>=1.8',
    'meshio',
    'rtree',
    'scikit-image',
    'open3d',
    'pillow',
    'rich',
]

setup(
    name='geotaichi',
    version='0.1.0',
    author='Shi-Yihao, Guo-Ning',
    author_email='',
    description='A High Performance Multiscale and Multiphysics Simulator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Yihao-Shi/GeoTaichi',
    packages=find_packages(include=['geotaichi', 'geotaichi.*', 'third_party', 'third_party.*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.8,<3.13',
    install_requires=requirements,
    include_package_data=True,
    package_data={
        'geotaichi': ['**/*.py'],
        'third_party': ['**/*.py'],
    },
    license='GPL-3.0',
    keywords='geomechanics simulation DEM MPM taichi',
)
