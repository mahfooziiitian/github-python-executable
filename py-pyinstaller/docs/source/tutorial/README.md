# Introduction

PyInstaller reads a Python script written by you. It analyzes your code to discover every other module and library your script needs in order to execute. Then it collects copies of all those files – including the active Python interpreter! – and puts them with your script in a single folder, or optionally in a single executable file.

- Creating a standalone executable from a Python script
- Adding icons or version info to the executable
- Bundling additional files (like images, data, or config files)
- Troubleshooting PyInstaller errors
- Creating a .spec file or customizing one

## Building executable

```bash
pyinstaller myscript.py
pyinstaller --onefile --windowed myscript.py
```

## Syntax

```bash
pyinstaller [options] script [script …] | specfile
```

PyInstaller analyzes myscript.py and:

Writes myscript.spec in the same folder as the script.

Creates a folder build in the same folder as the script if it does not exist.

Writes some log files and working files in the build folder.

Creates a folder dist in the same folder as the script if it does not exist.

Writes the myscript executable folder in the dist folder.