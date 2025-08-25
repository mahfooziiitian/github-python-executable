from distutils.core import setup
import py2exe

setup(
    windows=['wx_app.py'],
    options={"py2exe": {"includes": ["wx"]}}
)
