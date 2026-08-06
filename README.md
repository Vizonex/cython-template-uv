# Cython-Template-UV
A template repository for writing and automating the build process 
of a cython compiled python library. There are plans to try and get
it working with the uv package manager.

# This Repo comes with

- Cheatsheet Workflow template for working with and compiling & testing workflows
- Dependabot updater script.
- Pytest folder for running and working with pytest workflow will help trigger it 
  to work right.
- `setup.py` script for working with bigger projects.
- `pyproject.toml` file with dynamic `__version__` grabber using setuptools.
- `__init__.pyx` script for extending Cython support via `cimport` or `import` likewise.

## Why
I have too many projects that work with cython and many more could be coming in the future.
Knowing how my brain tends to work having a way to speedup the creation process of cython related projects felt needed and felt like the right thing to do
at some point in time. If you would like to contribute and make this project better such as 
improving the workflows it will help as I can give this information to help optimize pycares in the future.


# Credits
- [pycares](https://github.com/saghul/pycares) 
    - Cleaver workflow system for building things and has been used as a template for a large portion of things 
    since it's system as modular enough for my own needs. Since I borrowed it, it has lead me to discover cleaver ways on how to improve it including uploading wheel releases to the release page.

Let me know if you decide to use this template and feel free to send prs or issues if theres anything to improve upon.

- [winloop](https://github.com/Vizonex/winloop) 
    - Really good setup.py script and I give credit to those who helped me code it and make it how it is today.
Let me know if you decide to use this template and feel free to send prs or issues if theres anything to improve upon.
