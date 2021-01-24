from conans import ConanFile, CMake


class OpenalprConan(ConanFile):
    name = "openalpr"
    version = "2.4"
    license = "AGPL-3.0 License"
    homepage = "https://openalpr.com"
    url = "https://github.com/lucsch/openalpr"
    description = "Automatic License Plate Recognition library"
    topics = ("ALPR", "Computer-vision", "deep-learning")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    exports_sources = "CMakeLists.txt", "src/*", "config/*", "doc/*", "runtime_data/*"
    requires = [("opencv/3.4.12"),
                ("tesseract/4.1.1"), ("libwebp/1.1.0", "override"),
                ("log4cplus/2.0.5")]

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("alpr.h", dst="include", src="src/openalpr")
        self.copy("alpr_c.h", dst="include", src="src/openalpr")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*", dst="bin", src="bin")
        self.copy("*.defaults", dst="share/openalpr/config", src="config")
        self.copy("*", dst="share/openalpr/runtime_data", src="runtime_data")


    def package_info(self):
        self.cpp_info.libs = ["openalpr"]
