from distutils.core import setup
import py2exe

setup(
name = "Mal",
description = "Python-based App",
version = "1.0",
console=["rawpymal.py"],
options = {
		"py2exe": {
			"unbuffered": True,
			"optimize": 2,
			"bundle_files": 1,
			"packages":"ctypes",
			"includes": "base64,sys,socket,struct,time,code,platform,getpass,shutil"
		}
	}
)