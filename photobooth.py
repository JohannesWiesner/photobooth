from __future__ import print_function
import os, sys
from PIL import Image

# sys.path.append("/home/pi/Python-Thermal-Printer")
from Adafruit_Thermal import *

# Set Path to Photo (Change this Path)
photoPath = "/home/pi/photobooth/"

# photo name
photoName = "ghadir.jpg"

# resize parameters
photoResize = 512, 384

# Define printer (use 9600 baudrate)
printer = Adafruit_Thermal("/dev/serial0", 9600, timeout=5)

# Resize the high res photo to create thumbnail
Image.open(photoPath + photoName).resize(photoResize, Image.ANTIALIAS).save(photoPath + "thumbnail.jpg")

# Rotate the thumbnail for printing
Image.open(photoPath + "thumbnail.jpg").transpose(2).save(photoPath + "thumbnail-rotated.jpg")

# Print the foto
printer.begin(90) # Warmup time
printer.setTimes(40000, 3000) # Set print and feed times
printer.justify('C') # Center alignment
printer.printImage(Image.open(photoPath + "thumbnail-rotated.jpg"), True) # Specify image to print
printer.feed(2)
printer.sleep()      # Tell printer to sleep
printer.wake()       # Call wake() before printing again, even if reset
printer.setDefault() # Restore printer to defaults