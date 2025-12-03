# Migration Guide: Package Structure Changes

## Overview

This document describes the package structure changes made to fix the pip installation issue and ensure Python 3.14 compatibility.

## Problem

The original GeoTaichi package had the following issues:

1. **Import Error**: The `geotaichi/__init__.py` imported from a sibling `src/` directory using `from src import ...`, which caused `ModuleNotFoundError: No module named 'src'` when the package was installed via pip.

2. **Missing Package Configuration**: No `setup.py` or `pyproject.toml` existed for proper pip installation.

## Solution

### 1. Package Structure Reorganization

**Before:**
```
GeoTaichi/
├── geotaichi/
│   └── __init__.py (importing from src)
├── src/
│   ├── __init__.py
│   ├── dem/
│   ├── mpm/
│   ├── sdf/
│   ├── utils/
│   └── ...
└── ...
```

**After:**
```
GeoTaichi/
├── geotaichi/
│   ├── __init__.py (using relative imports)
│   ├── dem/
│   ├── mpm/
│   ├── sdf/
│   ├── utils/
│   └── ...
├── src/ (kept for backward compatibility but not used)
└── ...
```

### 2. Import Changes

All imports were updated from absolute `src` imports to relative imports:

**Before:**
```python
from src import DEM, MPM, DEMPM
from src.sdf.BasicShape import arbitrarily
import src.utils.GlobalVariable as GlobalVariable
```

**After:**
```python
from .dem.mainDEM import DEM
from .mpm.mainMPM import MPM
from .sdf.BasicShape import arbitrarily
from .utils import GlobalVariable
```

### 3. Files Modified

- **geotaichi/__init__.py**: Updated all imports to use relative imports
- **179 Python files**: Updated `from src.` to `from ..` or `from .`
- **2 files with self-references**: Fixed imports like `from ..sdf import X` to `from . import X`

### 4. New Files

- **setup.py**: Traditional setuptools configuration
- **pyproject.toml**: Modern PEP 517/518 configuration
- Updated **.gitignore**: Allow setup.py, ignore build artifacts

## Installation

### For Users

```bash
# Install from source
pip install git+https://github.com/mkt-kuno/GeoTaichi.git

# Or clone and install
git clone https://github.com/mkt-kuno/GeoTaichi.git
cd GeoTaichi
pip install .
```

### For Developers

```bash
# Install in editable mode
git clone https://github.com/mkt-kuno/GeoTaichi.git
cd GeoTaichi
pip install -e .
```

## Compatibility

- **Python Versions**: 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14
- **Operating Systems**: Windows, Linux, macOS
- **Architecture**: x86_64, ARM64 (Apple Silicon)

## Usage

No changes to user code are required. The package still works the same way:

```python
from geotaichi import *

init()

mpm = MPM()
# ... rest of your code
```

## Notes

- The original `src/` directory is kept for backward compatibility with development setups that have `PYTHONPATH` configured.
- All examples and tests work without modification.
- The package can now be published to PyPI if desired.

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'src'"

**Solution**: This issue is fixed in the new version. Make sure you're using the latest code and have reinstalled the package:

```bash
pip uninstall geotaichi
pip install -e .  # or pip install .
```

### Issue: "ImportError: cannot import name 'gmsh' from 'trimesh.interfaces'"

**Solution**: This is a version compatibility issue. The code now handles this gracefully. The gmsh functionality will only be available if you have a compatible version of trimesh. This does not affect most functionality.

## Migration Checklist

If you're maintaining a fork or derivative:

- [ ] Copy all contents from `src/` into `geotaichi/`
- [ ] Update all `from src.` imports to relative imports
- [ ] Fix self-referencing imports (e.g., `from ..module import X` when already in module)
- [ ] Add `setup.py` and `pyproject.toml`
- [ ] Update `.gitignore`
- [ ] Test pip installation
- [ ] Verify all examples still work
