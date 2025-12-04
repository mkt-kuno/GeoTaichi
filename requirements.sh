#!/bin/bash
# Install GeoTaichi dependencies
# Python version requirement: >= 3.9, < 3.13

python3 -m pip install --upgrade pip
python3 -m pip install "taichi>=1.7.2,<1.8.0" scipy trimesh imageio matplotlib psutil "pynvml>=11.4.1" "shapely>=1.8" meshio rtree scikit-image open3d numpy gmsh

