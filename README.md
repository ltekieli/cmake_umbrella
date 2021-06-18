# CMake umbrella project

This repository contains an example CMake project structure supporting libraries and applications.
It supports all-in-one build approach, as well as single component build.

The C++ dependencies for host build are managed by conan. Build supports also cross-compilation SDKs, such as Yocto or OpenEmbedded.

For testing particular component, a simple bintest python library is available, which allows running applications in a sandboxed environment.

# Usage
```
$ ./build.sh help
./build.sh <function>

Use one of the following functions:
  build_all
  build_separate
  build_together
  test_units
  test_components
  clean
```
