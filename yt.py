import argparse
import pyexiv2

def clearallmetadata(imgename,presere):
    metadata=pyexiv2.ImageData(imgename)
    metadata.read()
    metadata.clear()
    metadata.w