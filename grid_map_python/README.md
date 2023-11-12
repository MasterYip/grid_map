
# Feature : Adding Python bindings
limaanto commented on Jan 12, 2022

Hi, first of all thank you for this wonderful library.  
I recently implemented Python bindings for my own use and saw in issue [#248](https://github.com/ANYbotics/grid_map/issues/248) that an interface with Python could be useful for the community.  
The Python bindings / interface is done with [pybind11](https://pybind11.readthedocs.io/) a mature and efficient open-source binding library that integrates well with ROS.  
For the moment I have only bound public functions of the `grid_map_core::GridMap` class (and their immediate dependencies) but more could easily be added, let me know.

# Main changes

- New package `grid_map_python` that will contain all the bindings containing:
    - `py_module.cpp` and `py_core.cpp` that generate the bindings library
    - A `setup.py` and `src/grid_map/__init__.py` that expose the module
    - A `tests` folder containing scripts to test bound functions from Python
- Interface with ROS messages: two `from_msg` and `to_msg` functions to bridge the bound object with native Python `grid_map_msgs/GridMap` structures.

# Exemple of usage

Using a `GridMap` object in a Python scripts is simply a matter of importing it from the `grid_map` module and calling its functions as with any Python object:

```python
from grid_map import GridMap
a = GridMap(['elevation', 'intensity', 'roughness'])
a.setGeometry([1,2], 0.5, [3, 10])
print(a)
# <1.00x2.00x0.50 grid on ['elevation', 'intensity', 'roughness'] at [ 3. 10.]>

a['elevation'][0,1:2] = 1
print(a['elevation'])
# [[nan,  1., nan, nan],
#  [nan, nan, nan, nan]]
```

Eigen matrices are exposed as numpy arrays (or compatibles) and vice-versa, making the use of `GridMap` frunctions straight-forward.

I have been using this for the past month and saw no performance issues or big limitations. The bindings are still incomplete but I think that partial coverage is better than no coverage. If people find it important to add other modules or class to the bindings, they can easily be added afterwards.