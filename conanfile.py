# The MIT License (MIT)
#
# Copyright (c) 2019 Mateusz Pusz
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from conans import ConanFile, CMake, tools

class CMCStl2Conan(ConanFile):
    name = "cmcstl2"
    version = "2019.03.18"
    description = "An implementation of C++ Extensions for Ranges"
    homepage = "https://github.com/CaseyCarter/cmcstl2"
    license = "https://github.com/CaseyCarter/cmcstl2/blob/master/LICENSE.txt"
    url = "https://github.com/mpusz/conan-cmcstl2"
    exports = ["LICENSE.md"]
    settings = "compiler"
    no_copy_source = True
    scm = {
        "type": "git",
        "url": "https://github.com/CaseyCarter/cmcstl2.git",
        "revision": "fb1b65b006e5df4be205cf538e360f8d16cda3ca"
    }
    generators = "cmake"

    def _configure_cmake(self):
        cmake = CMake(self)
        full_build = tools.get_env("CONAN_RUN_TESTS", False)
        cmake.definitions["STL2_BUILD_TESTING"] = full_build
        cmake.definitions["STL2_BUILD_EXAMPLES"] = full_build
        cmake.configure()
        return cmake

    def configure(self):
        if self.settings.compiler != "gcc" and self.settings.compiler != "clang":
            raise ConanInvalidConfiguration("Library cmcstl2 is only supported for gcc and clang")

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()
        if tools.get_env("CONAN_RUN_TESTS", False):
            cmake.test()

    def package(self):
        self.copy("license*", dst="licenses",  ignore_case=True, keep_path=False)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        if self.settings.compiler == "gcc":
            self.cpp_info.cxxflags = ["-fconcepts"]
        else:
            self.cpp_info.cxxflags = ["--Xclang -fconcepts-ts"]
