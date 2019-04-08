[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?maxAge=3600)](https://raw.githubusercontent.com/mpusz/conan-cmcstl2/master/LICENSE)
[![Travis CI](https://img.shields.io/travis/mpusz/conan-cmcstl2/master.svg?label=Travis%20CI)](https://travis-ci.org/mpusz/conan-cmcstl2)
[![Download](https://api.bintray.com/packages/mpusz/conan-mpusz/cmcstl2%3Ampusz/images/download.svg)](https://bintray.com/mpusz/conan-mpusz/cmcstl2%3Ampusz/_latestVersion)

# conan-cmcstl2

[conan-mpusz](https://bintray.com/mpusz/conan-mpusz) package for [C++ Extensions for Ranges](https://github.com/CaseyCarter/cmcstl2) library.

The package generated with this **conanfile** can be found at [conan-mpusz](https://bintray.com/mpusz/conan-mpusz/cmcstl2%3Ampusz).

`conan` client can be downloaded from [Conan.io](https://conan.io).

## Reuse the package

### Add conan-mpusz remote

To add [conan-mpusz](https://bintray.com/mpusz/conan-mpusz) remote to your
local `conan` instance run:

```bash
conan remote add conan-mpusz https://api.bintray.com/conan/mpusz/conan-mpusz
```

### Basic setup

```
$ conan install cmcstl2/2019.03.18@mpusz/stable --build=missing
```

### Project setup

If you handle multiple dependencies in your project, it would be better
to add a `conanfile.txt`

```
[requires]
cmcstl2/2019.03.18@mpusz/stable

[options]

[generators]
cmake_paths
```

or if you are using `conanfile.py` file add:

```python
requires = "cmcstl2/2019.03.18@mpusz/stable"
```

Complete the installation of requirements for your project running:

```
mkdir build
cd build
conan install .. --build=outdated <your_profile_and_settings>
<your typical build process>
```

Project setup installs the library (and all its dependencies), and assuming you chose
`cmake_paths` as a generator, it generates `conan_paths.cmake` file that defines variables
to make CMake `find_package()` work and find all the dependencies in the Conan local cache.


## Build package

```
$ conan create . <user>/<channel> <your_profile_and_settings>
```

## Upload package to server

```
$ conan upload -r <remote-name> --all cmcstl2/2019.03.18@<user>/<channel>
```
