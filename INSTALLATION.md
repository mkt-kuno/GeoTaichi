# GeoTaichi Installation Guide - Updated

## Python Version Requirements

GeoTaichi now supports Python 3.9 through 3.12:
- **Minimum version**: Python 3.9 (required for Taichi 1.7.2+)
- **Maximum version**: Python 3.12
- **Recommended version**: Python 3.11 or 3.12

## Installation Methods

### Method 1: Install using pip (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/Yihao-Shi/GeoTaichi
cd GeoTaichi
```

2. Install with pip:
```bash
pip install -e .
```

This will automatically install all required dependencies including:
- taichi >= 1.7.2
- numpy
- scipy
- matplotlib
- open3d
- trimesh
- meshio
- gmsh
- And other required packages

### Method 2: Install using uv (Modern Python Package Manager)

1. Install uv (if not already installed):
```bash
pip install uv
```

2. Clone the repository:
```bash
git clone https://github.com/Yihao-Shi/GeoTaichi
cd GeoTaichi
```

3. Install with uv:
```bash
uv pip install -e .
```

Or sync from the lock file:
```bash
uv pip sync requirements.txt
```

## Backend Support

GeoTaichi now supports multiple computational backends:

### CPU Backend
Always available, no additional setup required:
```python
from geotaichi import init
init(arch='cpu')
```

### GPU Backend (CUDA)
Requires NVIDIA GPU and CUDA drivers:
```python
from geotaichi import init
init(arch='gpu')  # Default, falls back to CPU if GPU unavailable
```

### Vulkan Backend (NEW)
Cross-platform GPU computing via Vulkan:
```python
from geotaichi import init
init(arch='vulkan', device_memory_GB=4.0)  # 4GB default for Vulkan
```

## Running Examples

After installation, test with the triaxial test example:

```bash
cd example/dem/TriaxialTest
python generate.py      # Generate sphere packing
python FillBox.py       # Fill the box with particles
python conso.py         # Consolidation test
python drained.py       # Drained triaxial test
python undrained.py     # Undrained triaxial test
```

## Troubleshooting

### GPU Not Available
If you see "Could not initialize NVIDIA GPU", the system automatically falls back to CPU mode. This is normal if you don't have an NVIDIA GPU.

### Import Errors
If you encounter import errors, try reinstalling:
```bash
pip install -e . --force-reinstall
```

### Python Version Issues
Verify your Python version:
```bash
python --version  # Should be 3.9 or higher
```

If you have multiple Python versions, use:
```bash
python3.11 -m pip install -e .
```
