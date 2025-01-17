from conans import ConanFile, CMake, tools
import os

class MSCLTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = ("cmake_paths", "cmake_find_package", "virtualrunenv")
    #options = {"shared": [True, False]}
    #default_options = {"shared": False}
    #requires = "boost/1.69.0"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        target_name = "TestTarget"
        if self.settings.os == "Windows":
            tester_exe = target_name + ".exe"
            tester_path = os.path.join(self.build_folder,
                                       str(self.settings.build_type))
        else:
            tester_exe = target_name
            tester_path = "." + os.sep
        self.run(os.path.join(tester_path, tester_exe),run_environment=True )
