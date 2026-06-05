from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext
import os

from importlib.util import find_spec

def package_exists(module: str) -> None:
    """Checks to see if a package exists without needing to import or execute it's code.

    :param module: the package's name 
    
    :returns: True if package was found, False if not.
    """
    return find_spec(module) is not None


# TODO: Make a seperate setup.py that can replace this one that uses a cmake command for accessing
# external libraries. (Maybe we can add nmake also Not sure...)


class my_build_ext(build_ext):
    # Brought over from winloop since these can be very useful.
    user_options = build_ext.user_options + [
        ("cython-always", None, "run cythonize() even if .c files are present"),
        (
            "cython-annotate",
            None,
            "Produce a colorized HTML version of the Cython source.",
        ),
        ("cython-directives=", None, "Cythion compiler directives"),
    ]

    def initialize_options(self) -> None:
        self.cython_always = False
        self.cython_annotate = False
        self.cython_directives = None
        super().initialize_options()

    # copied from winloop you have my permission to use this elsewhere as needed...
    def finalize_options(self) -> None:
        need_cythonize = self.cython_always
        cfiles = {}

        for extension in self.distribution.ext_modules:
            for i, sfile in enumerate(extension.sources):
                if sfile.endswith(".pyx"):
                    prefix, _ = os.path.splitext(sfile)
                    cfile = prefix + ".c"

                    if os.path.exists(cfile) and not self.cython_always:
                        extension.sources[i] = cfile
                    else:
                        if os.path.exists(cfile):
                            cfiles[cfile] = os.path.getmtime(cfile)
                        else:
                            cfiles[cfile] = 0
                        need_cythonize = True

        if need_cythonize:
            # Double check Cython presence in case setup_requires
            # didn't go into effect (most likely because someone
            # imported Cython before setup_requires injected the
            # correct egg into sys.path.
            if not package_exists("Cython"):
                raise RuntimeError(
                    "please install cython to compile this package from source"
                )

            from Cython.Build import cythonize

            directives = {}
            if self.cython_directives:
                for directive in self.cython_directives.split(","):
                    k, _, v = directive.partition("=")
                    if v.lower() == "false":
                        v = False
                    if v.lower() == "true":
                        v = True
                    directives[k] = v
                self.cython_directives = directives

            self.distribution.ext_modules[:] = cythonize(
                self.distribution.ext_modules,
                compiler_directives=directives,
                annotate=self.cython_annotate,
                emit_linenums=self.debug,
            )

        return super().finalize_options()


if __name__ == "__main__":
    setup(
        ext_modules=[
            Extension(
                "cython_template_uv._mod",
                ["src/cython_template_uv/_mod.pyx"]
            )
        ],
        cmdclass={"build_ext": my_build_ext},
    )
