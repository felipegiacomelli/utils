import os
import shutil


def DeleteFile(file):
    if os.path.exists(file):
        os.remove(file)


def DeleteDirectory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)


def MakeDirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def GetDirectoyFiles(directory, extension=".csv"):
    return sorted(
        [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]
    )
