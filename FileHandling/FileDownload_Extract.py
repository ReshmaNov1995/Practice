import wget
from zipfile import ZipFile
import patoolib


downloadpath="D:\sample"
wget.download("https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_win32.zip",downloadpath)

zipfilepath="D:\sample\chromedriver_win32.zip"
zip=ZipFile(zipfilepath)

ZipFile.extractall(zip,downloadpath)

print("AA")

# path,where to extract
# patoolib.extract_archive("D:\\dummy\\abc.rar","D:\\dummy")



