from conans import ConanFile

class CppSubprocess(ConanFile):
    name = "cpp-subprocess"
    version = "2.0"
    license = "MIT"
    url = "https://github.com/nextsilicon/cpp-subprocess"
    homepage = "https://github.com/nextsilicon/cpp-subprocess#readme"
    topics = ("subprocess", "os", "fork")
    description = ("Subprocessing with modern C++, "
                   "The only goal was to develop something that is as close as"
                   "python subprocess module in dealing with processes.")
    # No settings/options are necessary, this is header only
    exports_sources = "subprocess.hpp"
    no_copy_source = True
    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto"
    }

    def package(self):
        self.copy("subprocess.hpp", dst="include")

    def package_id(self):
        self.info.header_only()
