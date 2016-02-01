from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')


setup(windows=[{"script":'main.py',
                "icon_resources":[(1, "guitar.ico")]}], 
      data_files = [
            ('imageformats', [
              r'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qico4.dll'
              ])],
      zipfile = None,
      options={"py2exe":{'compressed': True, 
                         "includes":["sip"]}})