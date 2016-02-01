from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True,"includes":["sip"],'dll_excludes': ['crypt32.dll'],}},
    windows = [{'script': "main.py", "icon_resources": [(1, "guitar.ico")]}],
    zipfile = None,
)