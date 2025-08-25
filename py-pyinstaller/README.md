# PyInstaller

It bundles a Python application and all its dependencies into a single package.

The user can run the packaged app without installing a Python interpreter or any modules.

PyInstaller supports Python 3.8 and newer, and correctly bundles many major Python packages such as numpy, matplotlib, PyQt, wxPython, and others.

PyInstaller is tested against Windows, MacOS X, and Linux.

However, it is not a cross-compiler; to make a Windows app you run PyInstaller on Windows, and to make a Linux app you run it on Linux, etc.

PyInstaller has been used successfully with AIX, Solaris, FreeBSD and OpenBSD but testing against them is not part of our continuous integration tests, and the development team offers no guarantee (all code for these platforms comes from external contributions) that PyInstaller will work on these platforms or that they will continue to be supported.

## Convert into executable

    pyinstaller your_program.py

## Convert into a bundle

    pyinstaller --onefile your_program.py

## Convert into a bundle without console

    pyinstaller --onefile --noconsole your_program.py
