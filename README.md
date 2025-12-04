# GeoTaichi

![Github License](https://img.shields.io/github/license/Yihao-Shi/GeoTaichi)          ![Github stars](https://img.shields.io/github/stars/Yihao-Shi/GeoTaichi)          ![Github forks](https://img.shields.io/github/forks/Yihao-Shi/GeoTaichi)         [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 

[**Quick start**](#quick-start) | [**Examples**](#examples) | [**Paper**](https://www.researchgate.net/publication/380048019_GeoTaichi_A_Taichi-powered_high-performance_numerical_simulator_for_multiscale_geophysical_problems) | [**Citation**](#citation) | [**Contact**](#acknowledgements)

## Brief description

A [Taichi](https://github.com/taichi-dev/taichi)-based numerical package for high-performance simulations of multiscale and multiphysics geophysical problems. 
Developed by [Multiscale Geomechanics Lab](https://person.zju.edu.cn/en/nguo), Zhejiang University.

<p align="center">
    <img src="https://github.com/Yihao-Shi/GeoTaichi/blob/main/images/GeoTaichi.png" width="90%" height="90%" />
</p>


## Overview

GeoTaichi is a collection of several numerical tools, currently including __Discrete Element Method (DEM)__, __Material Point Method (MPM)__, __Material Point-Discrete element method (MPDEM)__, and __Finite Element Method (FEM)__, that cover the analysis of the __Soil-Gravel-Structure-Interaction__ in geotechnical engineering. The main components of GeoTaichi is illustrated as follows:
<p align="center">
    <img src="https://github.com/Yihao-Shi/GeoTaichi/blob/main/images/main_component.png" width="50%" height="50%" />
</p>

GeoTaichi is a research project that is currently __under development__. Our vision is to share with the geotechnical community a free, open-source (under the GPL-3.0 License) software that facilitates the relevant computational research. In the Taichi ecosystem, we hope to emphasize the potential of Taichi for scientific computing. Furthermore, GeoTaichi is high parallelized, multi-platform (supporting for Windows, Linux and Macs) and multi-architecture (supporting for both CPU and GPU).

## Examples

Have a cool example? Submit a [PR](https://github.com/Yihao-Shi/GeoTaichi/pulls)!

### Material point method (MPM)
| [Column collapse](example/mpm/ColumnCollapse/DPmaterial.py) | [Dam break](example/mpm/ColumnCollapse/NewtonianFluid.py) | [Strip footing](example/mpm/Footing/StripFootingTresca.py) | [Progressive failure process of sensitive clay](example/mpm/ColumnCollapse/SoftDP.py) |
| --- | --- | --- | --- |
| ![Column collapse](images/soil.gif) | ![Dam break](images/newtonian.gif) | ![Strip footing](images/footing.gif) | ![Clay](images/clay.gif) |

### Discrete element method (DEM)
| [Granular packing](example/dem/GranularPackings/polyLevelSet/packing_generate.py) | [Screw and nut](example/dem/ParticleSliding/screw_and_nut.py) | [Debris Flow](example/dem/DebrisFlow) | 
| --- | --- | --- | 
| ![Granular packing](images/lsdem.gif) | ![Screw and nut](images/screw_nut.gif) | ![Debris Flow](images/debris_flow.gif) | 

|[Rotating drum](example/dem/RotatingDrums) | [Triaxial shear test](example/dem/TriaxialTest) |
| --- | --- | 
| ![Rotating drum](images/drums.gif) | ![Triaxial shear test](images/force_chain.gif) |

### Coupled material point-discrete element method (MPDEM)
| [A sphere impacting granular bed](example/dempm/SphereImpact/plane_strain.py) | [Granular column impacting cubic particles](example/dempm/GranularImpact/granular_impact.py) | [Box sinking into water](example/dempm/BoxSinking/box.py) |
| --- | --- | --- |
| ![A sphere impacting granular bed](images/mpdem1.gif) | ![Granular column impacting cubic particles](images/mpdem2.gif) | ![Box sinking into water](images/box_sinking.gif) |

## Quick start

### Installation

GeoTaichi can be installed using multiple methods depending on your preference and environment.

#### Method 1: Install with pip (Recommended for most users)

The simplest way to install GeoTaichi:

```bash
# Clone the repository
git clone https://github.com/Yihao-Shi/GeoTaichi
cd GeoTaichi

# Install with pip
pip install .

# Or install in editable mode for development
pip install -e .
```

**With optional dependencies:**
```bash
# Install with GPU support
pip install -e ".[gpu]"

# Install with mesh processing support (gmsh)
pip install -e ".[mesh]"

# Install with all optional dependencies
pip install -e ".[all]"
```

#### Method 2: Install with uv (Fast and modern)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver:

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/Yihao-Shi/GeoTaichi
cd GeoTaichi

# Create a virtual environment and install
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install the package
uv pip install -e .

# Or with optional dependencies
uv pip install -e ".[all]"
```

#### Method 3: Install with Conda/Mamba (Cross-platform)

For users who prefer conda environments:

```bash
# Clone the repository
git clone https://github.com/Yihao-Shi/GeoTaichi
cd GeoTaichi

# Create and activate conda environment
conda env create -f geotaichi_env.yml
conda activate geotaichi

# Install GeoTaichi in the environment
pip install -e .
```

**Note:** After conda environment creation, you may need to install the package itself:
```bash
conda activate geotaichi
pip install -e .
```

#### Method 4: Install from source (Advanced users)

For development or custom builds:

```bash
# Clone the repository
git clone https://github.com/Yihao-Shi/GeoTaichi
cd GeoTaichi

# Install dependencies
bash requirements.sh

# Set up Python path (Linux/Mac)
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Or on Windows
set PYTHONPATH=%PYTHONPATH%;%CD%
```

### System Requirements

**Minimum Requirements:**
- Python 3.8 or higher
- 4GB RAM (8GB+ recommended)
- CPU with AVX2 support

**GPU Requirements (Optional but recommended for large simulations):**
- NVIDIA GPU with CUDA support
- CUDA Toolkit 11.0 or higher
- cuDNN (for optimal performance)

**Platform Support:**
- ✅ Linux (Ubuntu 18.04+, CentOS 7+)
- ✅ Windows 10/11
- ✅ macOS 10.15+ (CPU and Metal GPU support)

### Known Dependency Issues

**Issue 1: gmsh library dependencies**
- `gmsh` requires system library `libGLU.so.1` on Linux
- **Solution:** `sudo apt-get install libglu1-mesa` (Ubuntu/Debian)
- Or install with: `pip install -e ".[mesh]"` only if needed

**Issue 2: open3d on some systems**
- `open3d` may have compatibility issues with older systems
- **Solution:** Try installing specific version: `pip install open3d==0.17.0`

**Issue 3: shapely with spatial indexing**
- `rtree` requires `libspatialindex`
- **Solution (Ubuntu/Debian):** `sudo apt-get install libspatialindex-dev`
- **Solution (macOS):** `brew install spatialindex`

**Issue 4: GPU support**
- NVIDIA GPU support requires CUDA toolkit installation
- See [CUDA Installation Guide](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
- macOS uses Metal backend automatically (no CUDA needed)

### Verifying Installation

After installation, verify GeoTaichi is working:

```python
# Test import
from geotaichi import *

# Initialize (CPU mode for testing)
init(arch="cpu")

# Create a simple DEM simulation
dem = DEM()
print("✓ GeoTaichi installed successfully!")
```

### Troubleshooting

If you encounter import errors:

1. **ModuleNotFoundError for geotaichi:**
   - Ensure you installed the package: `pip install -e .`
   - Check Python path: `python -c "import sys; print(sys.path)"`

2. **CUDA/GPU errors:**
   - Verify CUDA installation: `nvidia-smi`
   - Use CPU mode for testing: `init(arch="cpu")`

3. **Dependency conflicts:**
   - Create a fresh virtual environment
   - Install with uv for better dependency resolution: `uv pip install -e .`

For more issues, see [GitHub Issues](https://github.com/Yihao-Shi/GeoTaichi/issues) or the [Migration Guide](MIGRATION_GUIDE.md).

### Quick Start Examples

After installation, try running examples:

```bash
# Run a simple DEM example
cd example/dem/RotatingDrums
python rotating_drum.py

# Run an MPM example
cd example/mpm/ColumnCollapse
python DPmaterial.py
```

**Note:** Modify `init()` calls based on your hardware:
- For CPU: `init(arch="cpu")`
- For GPU: `init(arch="gpu")`
- For macOS GPU: `init(arch="metal")`

### Working with vtu files

To visualize the VTS files produced by some of the scripts, it is recommended to use [ParaView](http://www.paraview.org/). To visualize the output in ParaView, use the following
procedure:
1. Open the .vts or .vtu file in ParaView
2. Click on the "Apply" button on the left side of the screen
3. Make sure under "Representation" that "Surface" or "Surface with Edges" is selected
4. Under "Coloring" select variables and the approriate measure (i.e. "Magnitude", X-direction displacement, etc.)

### Document

Currently, only the tutorial of DEM in Chinese version is available in [doc](https://github.com/Yihao-Shi/GeoTaichi/blob/main/docs/GeoTaichi_tutorial_DEM_Chinese_version.pdf). 
Users can set up simulations by specifying numerical parameters and configuring the desired simulation settings in a Python script. More detailed about Python scripts can be found in the [example floder](https://github.com/Yihao-Shi/GeoTaichi/tree/main/example).

## Features
### Discrete Element Method 
Discrete element method is a powerful tool to simulate the movement of granular materials through a series of calculations that trace individual particles constituting the granular material.
  - Sphere, multisphere particles and level-set DEM
  - Unified approach for creating level-set functions for irregularly shaped particle
  - Generating particle packings by specifying initial void ratio or particle number in a box/cylinder/sphere/triangular prism
  - Three neighbor search algorithms, brust search/linked-cell/multilevel linked-cell
  - Two velocity updating schemes, symlectic Euler/velocity Verlet
  - Four contact models, including linear elastic, hertz-mindlin, linear rolling and energy conserving model
  - Supporting plane (infinite plane)/facet (servo wall)/triangle patch (suitable for complex boundary condition)
  - Supporting [periodic boundary](example/dem/PeriodicBoundary) for sphere particles

### Material Point Method 
The material point method (MPM) is a numerical technique used to simulate the behavior of solids, liquids, gases, and any other continuum material. Unlike other mesh-based methods like the finite element method, MPM does not encounter the drawbacks of mesh-based methods (high deformation tangling, advection errors etc.) which makes it a promising and powerful tool in computational mechanics. 
  - Nine Constitutive Models, including linear elastic/neo-hookean/Von-Mises/isotropic hardening plastic/(state-dependent) Mohr-Coulomb/Drucker-Prager/(cohesive) modified cam-clay/Newtonian fluid/Bingham fluid
  - Two improved velocity projection techniques, including TPIC/APIC/MLS
  - Three stress update schemes, including USF/USL/MUSL
  - Three stabilization techniques, including mix integration/B-bar method/F-bar method
  - Two smoothing mehod, including strain/pressure smoothing
  - Supporting Dirichlet (Fix/Reflect/Friction)/Neumann boundary conditions
  - Supporting total/updating Lagrangian explicit MPM 
  - Free surface detection
  - Supporting input [external CAD files](example/mpm/ExternalOBJ)

### MPDEM coupling
  - Two contact models, including linear elastic, hertz-mindlin, Energy conserving model (Barrier functions)
  - Support DEM-MPM-Mesh contact, feasible simulating complex boundary conditions 
  - Multilevel neighbor search
  - Two way or one way coupling

### Postprocessing
  - Restart from a specific time step
  - A simple GUI powered by [Taichi](https://github.com/taichi-dev/taichi)
  - VTU([Paraview](http://www.paraview.org/)) and NPZ(binary files) files are generated in the process of simualtion
  - Supporting force chain visualization

## Under development
  - Developing a well-structured IGA modules
  
## License
This project is licensed under the GNU General Public License v3 - see the [LICENSE](https://www.gnu.org/licenses/) for details.

## Citation
Please kindly star :star: this project if it helps you. We take great efforts to develope and maintain it :grin::grin:.

If you publish work that makes use of GeoTaichi, we would appreciate if you would cite the following reference:
```latex
@article{shi2024geotaichi,
  title={GeoTaichi: A Taichi-powered high-performance numerical simulator for multiscale geophysical problems},
  author={Shi, YH and Guo, N and Yang, ZX},
  journal={Computer Physics Communications},
  volume={301},
  pages={109219},
  year={2024},
  publisher={Elsevier}
}
@article{shi2025gpu,
  title={GPU-accelerated level-set DEM for arbitrarily shaped particles with broad size distributions},
  author={Shi, YH and Guo, N and Yang, ZX},
  journal={Powder Technology},
  pages={121293},
  year={2025},
  publisher={Elsevier}
}
```

## Acknowledgements
We thank all amazing contributors for their great work and open source spirit. We welcome all kinds of contributions to file an issue at [GitHub Issues](https://github.com/Yihao-Shi/GeoTaichi/issues).

### Contributors
<a href="https://github.com/Yihao-Shi/GeoTaichi/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Yihao-Shi/GeoTaichi" />
</a>

### Contact us
- If you spot any issue or need any help, please mail directly to <a href = "mailto:shiyh@zju.edu.cn">shiyh@zju.edu.cn</a>.

## Release Notes
V0.4.0 (Aug 27, 2025)

- Please click [here](https://github.com/Yihao-Shi/GeoTaichi/releases/tag/GeoTaichi-v0.4) for more details

V0.3.0 (December 12, 2024)

- Please click [here](https://github.com/Yihao-Shi/GeoTaichi/releases/tag/GeoTaichi-v0.3) for more details

V0.2.2 (July 22, 2024)

- Fix computing the intersection area between circles and triangles
- Add "Destory" and "Reflect" boundaries in DEM modules, see [examples](https://github.com/Yihao-Shi/GeoTaichi/blob/main/example/dem/SimpleChute/simple_chute.py)

V0.2 (July 1, 2024)

- Fix some bugs in DEM and MPM modules, see [details](https://github.com/Yihao-Shi/GeoTaichi/releases/tag/GeoTaichi-v0.2)
- Add some advanced constitutive model

V0.1 (January 21, 2024)

- First release GeoTaichi
